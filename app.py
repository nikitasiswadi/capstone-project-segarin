from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import get_file
from back_end import Mysql,GCStorage
import os
import io
from google.cloud import storage


model_kubis = load_model("model_kubis.h5")
model_bayam = load_model("model_bayam.h5")
model_kangkung = load_model("model_kangkung.h5")
""" 
img_url = 'https://storage.googleapis.com/segarin_bucket/kubis/gambar2.jpg'
random_string_for_file_name = img_url.split("/")[5]
print(random_string_for_file_name)
img = image.load_img(get_file(random_string_for_file_name,img_url),target_size=(256,256))
x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x,axis = 0)

images = np.vstack([x])
classes = model_test.predict(images, batch_size=10)
print(classes)
output_class= np.argmax(classes)
classname = ['Busuk', 'Segar']
print("The predicted class is", classname[output_class]) """

app = Flask(__name__)

mysql = Mysql("localhost","root","","DatabaseSegarin")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'project_segarin.json'

gcs = GCStorage(storage.Client())
bucket_name = "segarin_bucket"

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/getUser",methods=["POST","GET"])
def getUser():
    data = [string[x] for x in request.form.values()]
    return print(mysql.get_user(data[0],data[1]))

@app.route("/getListUser",methods=["GET"])
def getListUser():
    return mysql.get_list_user()

@app.route("/insertUser",methods=["POST"])
def insertUser():
    data = [string[x] for x in request.form.values()]
    return print(insert_user(data[0],data[2],data[1]))

@app.route("/fotoKubis", methods =["POST"])
def fotoKubis():
    data=  request.files['test']
    tipe = data.content_type
    gcs.upload_file(bucket_name,os.path.join("kubis/",str(data.filename)),data.read(),tipe)
    img = Image.open(data)
    data = io.BytesIO()
    img.save(data, "JPEG")
    img = image.load_img(data,target_size=(256,256))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x,axis = 0)

    images = np.vstack([x])
    classes = model_kubis.predict(images, batch_size=10)
    output_class= np.argmax(classes)
    classname = ['Busuk', 'Segar']
    
    return ("The predicted class is "+ str(classname[output_class]))

@app.route("/fotoBayam", methods =["POST"])
def fotoBayam():
    data=  request.files['test']
    tipe = data.content_type
    gcs.upload_file(bucket_name,os.path.join("bayam/",str(data.filename)),data.read(),tipe)
    img = Image.open(data)
    data = io.BytesIO()
    img.save(data, "JPEG")
    img = image.load_img(data,target_size=(128,128))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x,axis = 0)

    images = np.vstack([x])
    classes = model_bayam.predict(images, batch_size=10)
    output_class= np.argmax(classes)
    classname = ['Busuk', 'Segar']
    
    return ("The predicted class is "+ str(classname[output_class]))

    """ return  """

@app.route("/fotoKangkung", methods =["POST"])
def fotoKangkung():
    data=  request.files['test']
    tipe = data.content_type
    gcs.upload_file(bucket_name,os.path.join("kangkung/",str(data.filename)),data.read(),tipe)
    img = Image.open(data)
    data = io.BytesIO()
    img.save(data, "JPEG")
    img = image.load_img(data,target_size=(256,256))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x,axis = 0)

    images = np.vstack([x])
    classes = model_kangkung.predict(images, batch_size=10)
    output_class= np.argmax(classes)
    classname = ['Busuk', 'Segar']
    
    return ("The predicted class is "+ str(classname[output_class]))





