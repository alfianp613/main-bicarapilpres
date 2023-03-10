from flask import Flask, redirect, url_for, request
from flask.templating import render_template
from numpy import random
import pandas as pd
import joblib
import requests
from req_api import *

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('Welcome.html')

@app.route('/aboutus')
def AboutUs():
    return render_template('About Us.html')

@app.route('/candidate')
def candidate():
    return render_template('Infopedia Kandidat.html')
@app.route('/anies')
def anies():
    times = req('anies','http://143.198.206.37:5000/')
    return render_template('Anies.html',time=times)
@app.route('/ahy')
def ahy():
    times = req('ahy','http://143.198.206.37:5000/')
    return render_template('AHY.html',time=times)
@app.route('/ganjar')
def ganjar():
    times = req('ganjar','http://143.198.206.37:5000/')
    return render_template('Ganjar.html',time=times)
@app.route('/prabowo')
def prabowo():
    times = req('prabowo','http://143.198.206.37:5000/')
    return render_template('Prabowo.html',time=times)
@app.route('/ridwan')
def rk():
    times = req('rk','http://143.198.206.37:5000/')
    return render_template('Ridwan Kamil.html',time=times)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug = True,port=5001)
