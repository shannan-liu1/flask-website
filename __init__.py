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
