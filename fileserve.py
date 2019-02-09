""" Simple flask app for serving static files """

import os
import re
from flask import Flask, render_template, request, send_file
import conf
app = Flask(__name__)

@app.route('/')
def index():
    """ Empty path gives 404 so we need a separate endpoint for home """
    resources = conf.BaseConfig.FILES_BASE_PATH
    return render_template('index.html', files=os.listdir(resources), path='')

@app.route('/<path:path>')
def file_path(path):
    """ Take an arbitrary path and return the files or file """
    resources = conf.BaseConfig.FILES_BASE_PATH
    print(path)
    print(os.path.isdir(resources+path))
    if os.path.isdir(resources+path):
        return render_template('index.html', files=os.listdir(resources+path), path=path)

    return send_file(resources+path)
