from flask import Flask,jsonify,request,render_template
#from keras.models import load_model
import keras
from keras.applications import VGG16
import cv2  #success love successful company
import numpy as np
import os
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app = Flask(__name__)
modeldata = VGG16(weights='imagenet',input_shape=(300,300,3),include_top=False)
@app.route('/x',methods=['GET'])
def Index_Function():

    image = cv2.imread('download.jpg')
    
@app.route("/")
def function():
    img = cv2.imread("cats.png")
    ximg = cv2.resize(img,(300,300))
    result = modeldata.predict(ximg.reshape(-1,300,300,3))
    print(result)
    return 's'
@app.route("/show_image",methods=['POST'])
def GetData():
    data = request
    #p = modeldata.predict(image)
    decoded_image = cv2.imdecode(np.fromstring(data.data,np.uint8()),cv2.IMREAD_COLOR)
    cv2.imshow('image',decoded_image)
    cv2.waitKey(0)

    return "receifnsakved"
@app.route("/stinger/<string>/<quantity>")
def GenerateString(string,quantity):
    try:
        xdata = {'string':string*int(quantity)}
        return render_template("index.html",data=xdata)
    except Exception as e:
        return str(e)
    #return str(p)
if __name__ == '__main__':
    app.run(debug=True)