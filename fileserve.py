import os
from flask import Flask, render_template, request
import conf
app = Flask(__name__)

@app.route('/')
def index():
    resources = conf.BaseConfig.FILES_BASE_PATH
    return render_template('index.html', files=os.listdir(resources), path='')

@app.route('/<path:path>')
def file_path(path):
    resources = conf.BaseConfig.FILES_BASE_PATH
    return render_template('index.html', files=os.listdir(resources+path), path=path)
