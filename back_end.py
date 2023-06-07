import os 
import pathlib
import pymysql
from google.cloud import storage 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my-project-segarin-26678-bfc7835d7a7d.json'
STORAGE_CLASSES = "STANDAR"

""" mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
 """ 

class Mysql:
    def __init__(self, host, user, password, database):
        self.mydb = pymysql.connect(host=host, user=user, password=password,database=database)
    
    def get_user(self, id_user,password):
        mycursor = mydb.cursor()
        query = "SELECT * FROM pengguna WHERE username = {id_user} & password = {password}"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if(len(myresult)>0):
            return True
        else:
            return False
    
    def insert_user(self, id_user, password, email):
        mycursor = mydb.cursor()
        query = "INSERT INTO pengguna VALUES({id_user},{password},{email})"
        mycursor.execute(query)

        self.mydb.commit()
        if(mycursor.rowcount>0):
            return True
        else:
            return False

    def insert_foto(self,id_user,nama_file,keterangan=""):
        mycursor - mydb.cursor()
        query ="INSERT INTO pengguna VALUES({id_user},{nama_file},{keterangan})"
        mycursor.execute(query)
        self.mydb.commit()
        if(mycursor.rowcocunt>0):
            return True
        else:
            return False

class GCStorage :
    def __init__(self, client_storage):
        self.client = client_storage

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
        files = self.client.list_blobs(bucket_name) #bisa menggunakan (foldername) pada argumentnya ex : ('bayam/') dan gunakan split untuk mendapatkan nama filenya
        return [file.name for file in files]
    
    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)


def main():
    bucket_name = "test_bucket_segarin"
    gcs = GCStorage(storage.Client())
    gcs_labs = gcs.list_blobs(bucket_name)

    for blob in gcs_labs:
        path_download = os.getcwd()
        blob.download_to_filename(os.path.join(path_download,blob.name))
main()