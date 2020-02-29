import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input,decode_predictions
import os
from flask import Flask,render_template,jsonify
import cv2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
app = Flask(__name__)
modeldata = VGG16()
@app.route('/')
def Home():
    img = cv2.imread('cats.png')
    img = cv2.resize(img,(224,224))
    img = img.reshape(1,224,224,3)
    img = preprocess_input(img)
    ydata = modeldata.predict(img)
    r = decode_predictions(ydata)
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)