from flask import Flask, g, render_template, request
from flask.cli import with_appcontext
from werkzeug.security import check_password_hash, generate_password_hash

import click

import random
import string

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64

import sqlite3 # interface with the db


### stuff from last class
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

def get_message_db():
    """
    Handles creating database messages
    """
    try:
        return g.message_db
    except:
        # check if message_db exists in the g attribute
        # of our application
        # if not, create it
        g.message_db = sqlite3.connect("message_db.sqlite")
        cmd = """
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        handle TEXT NOT NULL,
        message TEXT NOT NULL
        );
        """
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db


def insert_message(request):
    cmd = """\
    
    """
    <input type="text" name="message" id="message">

def close_message_db(e = None):
    db = g.pop('message_db',None)
    if db is not None:
        db.close()

def init_db():
    db = get_message_db()



    #Check whether there is a database called message_db in the g attribute of the app. If not, then connect to that database, ensuring that the connection is an attribute of g. To do this last step, write a line like do g.message_db = sqlite3.connect("messages_db.sqlite")
