import os 
import pathlib
import json
import pymysql
from google.cloud import storage 
from flask import Flask, render_template, request, jsonify
from keras.models import load_model

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my-project-segarin-26678-bfc7835d7a7d.json'
STORAGE_CLASSES = "STANDAR"


class Mysql:
    def __init__(self, host, user, password, database):
        self.mydb = pymysql.connect(host=host, user=user, password=password,database=database)
    
    def get_user(self, username ,password):
        mycursor = self.mydb.cursor()
        query = "SELECT * FROM Profile WHERE Username =%s && Password =%s"
        data = (username,password)
        mycursor.execute(query,data)
        myresult = mycursor.fetchall()
        if(len(myresult)>0):
            return True
        else:
            return False

    def get_list_user(self):
        mycursor = self.mydb.cursor()
        query = "SELECT * FROM Profile"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if(len(myresult)>0):
            content_data =[]
            user = {}
            for data in myresult:
                content ={'id': data[0], 'username': data[1],'email': data[2],'password': data[3]}
                content_data.append(content)
                content ={}
            return content_data
        else:
            return False
    
    def insert_user(self, username, password, email):
        mycursor = self.mydb.cursor()
        query = "INSERT INTO Profile(Username,Email,Password) VALUES(%s,%s,%s)"
        data = (username,password,email)
        mycursor.execute(query,data)

        self.mydb.commit()
        if(mycursor.rowcount>0):
            return True
        else:
            return False

    def insert_foto(self,id_user,nama_file, TipeSayur, keterangan=""):
        mycursor = self.mydb.cursor()
        query ="INSERT INTO foto VALUES(%s,%s,%s,%s)"
        data = (id_user,nama_file,TipeSayur,keterangan)
        mycursor.execute(query,data)
        self.mydb.commit()
        if(mycursor.rowcount>0):
            return True
        else:
            return False

    def get_list_foto(self):
        mycursor = self.mydb.cursor()
        query = "SELECT * FROM foto"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if(len(myresult)>0):
            content_data =[]
            for data in myresult:
                content ={'id': data[0], 'username': data[1],'email': data[2],'password': data[3]}
                content_data.append(content)
                content ={}
            return content_data
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
    """ bucket_name = "test_bucket_segarin"
    gcs = GCStorage(storage.Client())
    gcs_labs = gcs.list_blobs(bucket_name)
 """
    mysql = Mysql("localhost","root","","DatabaseSegarin")

    print(mysql.get_list_foto())
main()