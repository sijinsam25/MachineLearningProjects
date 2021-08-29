# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:25:33 2021

@author: LENOVO
"""

from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import pickle
#import numpy as np
#from joblib import load

#from sklearn.neural_network import MLPClassifier

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

def predict():
    audio=file_upload("select an audio:",accept="audio/*")
    
    prediction = model.predict([[audio]])
    
    put_text('student willbe:',prediction)
    
app.add_url_rule('/emotion', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    predict()
    
app.run(host='localhost', port=80)

# model =load(open('filename.joblib','rb'))



