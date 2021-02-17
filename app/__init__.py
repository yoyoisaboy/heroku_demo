# -*- coding: UTF-8 -*-

import numpy as np
import os

from flask import Flask, request, render_template
from flask_cors import CORS
from app.machineLearning_test import test


app = Flask(__name__)
CORS(app)

PEOPLE_FOLDER = os.path.join('static', 'result_plot')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER



@app.route('/page1', methods=['GET'])
def getpage():
    
    return "page1"

@app.route('/pic', methods=['GET'])
def getResult():
    
    picture = test()
    if picture != None:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], picture)
        return render_template('layout.html',pic = full_filename)
    else:
        return "None"