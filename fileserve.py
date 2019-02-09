import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    resources = './rec/'
    return render_template('index.html', files=os.listdir(resources), path='/')

@app.route('/<path:path>')
def file_path(path):
    resources = './rec/'
    return render_template('index.html', files=os.listdir(resources+path), path=path)
