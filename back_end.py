import os 
import pathlib
import pymysql
from google.cloud import storage 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my-project-segarin-26678-bfc7835d7a7d.json'
STORAGE_CLASSES = "STANDAR"

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

class GCStorage :
    def __init__(self, client_storage):
        self.client = client_storage
    def create_bucket(self, bucket_name, storage_class, bucket_location="ASIA-SOUTHEAST2"):
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = storage_class
        bucket.location= bucket_location;
        return self.client.create_bucket(bucket,bucket_location)
    
    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)
    
    def list_buckets(self):
        buckets = self.client.list_buckets()
        return [bucket for bucket in buckets]

    def upload_file(self, bucket, file_destination, file_path):
        blob = bucket.blob(file_destination)
        blob.upload_from_filename(file_path)
        return blob
    
    def list_nama_blobs(self, bucket_name):
        files = self.client.list_blobs(bucket_name)
        return [file.name for file in files]
    
    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)


def main():
    bucket_name = "test_bucket_segarin"
    gcs = GCStorage(storage.Client())
    print(gcs.list_nama_blobs(bucket_name)[0].split(".")[1])

main()