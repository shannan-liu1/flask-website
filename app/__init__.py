from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64

### stuff from last class
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about/', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

# Request object: https://flask.palletsprojects.com/en/2.1.x/api/#flask.Request
@app.route('/submit-basic/', methods=['POST', 'GET'])
def submit_basic():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            # this is how to access the upladed file
            # img = request.files['image']
            return render_template('submit.html',thanks = True)
        except:
            return render_template('submit.html', error = True)
