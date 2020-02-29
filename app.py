from flask import Flask,jsonify,request,render_template,request
import cv2
from keras.models import load_model
#from keras.models import model_from_json,load_model
import  json
import numpy as np
import keras.backend.tensorflow_backend as tb
import os
import  matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app = Flask(__name__)
''''
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
'''
loaded_model = load_model('cats_and_dogs_small_2.h5')
@app.route("/x")
def Hoome():
    img = cv2.imread('download.jpg')
    ximg = cv2.resize(img,(150,150))
    result = loaded_model.predict(ximg.reshape(1,150,150,3))
    
    if result == 1.:
        return render_template('index.html',r = 'Dog')
    elif result == 0.:
        return render_template('index.html',r = 'Cat')
    
@app.route("/")
def Upload_image():
    return render_template('upload_image.html')
@app.route("/show_image",methods=['POST'])
def Show_image():
    img = request.files.get('data')
    print(type(img))
    return 'ok'
if __name__ == "__main__":
    app.run(debug=False,threaded=False)