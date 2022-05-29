from flask import Flask, g, render_template, request
import sqlite3 # for interfacing with our db

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

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('main.html')

def get_message_db():
    """
    Handles creating database messages
    """
    # check if message_db exists in the g attribute
    # of our application
    # if not, create it
    try:
        return g.message_db # return db if it already exists
    except:
        # create message db
        g.message_db = sqlite3.connect("message_db.sqlite")

        # sql command to create table called messages in message db
        cmd = """
        CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        handle TEXT NOT NULL,
        message TEXT NOT NULL
        );
        """
        
        # execute the db command 
        # with cursor object
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db

def insert_message():
    """
    Called when the user submits their handle and message on the
    submit page of our website
    """

    # use request object to get user's handle & message input
    handle = request.form['handle']
    message = request.form['message']
    db = get_message_db()

    cmd = f"""
    INSERT INTO messages (handle, message) 
    VALUES ('{handle}', '{message}')
    """

    # execute the db command 
    # with cursor object
    cursor = db.cursor()
    cursor.execute(cmd)

    # save changes to db and close connection
    db.commit()
    db.close()
    return handle, message

@app.route('/submit', methods=['POST', 'GET'])
def submit():

    # show this page for when user doesn't make a submission
    if request.method == 'GET':
        return render_template('submit.html')
    # otherwise, if the user has made a submission,
    # show this page
    else:
        # call insert_message() 
        # render template w/ new variables
        # retrieved from intert_message() function
        try:
            handle, message = insert_message()
            return render_template('submit.html', submitted=True, message=message, handle=handle)
        except: # if an error occurred, render the webpage while specifying the error
            return render_template('submit.html', error=True)

def random_messages(n):
    # open connection to db
    db = get_message_db()

    # randomly select n handles and messages to display
    cmd = f"""
    SELECT * FROM messages ORDER BY RANDOM() LIMIT {n}
    """

    # execute the db command 
    # with cursor object
    cursor = db.cursor()
    cursor.execute(cmd)

    # use fetchall to get the n randomly selected 
    # handles and messages in our database
    message_info = cursor.fetchall()
    db.close() #  close connection
    
    return message_info

@app.route('/view/')
def view():
    # view messages
    return render_template('view.html', messages=random_messages(10))
    