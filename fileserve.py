""" Simple flask app for serving static files """

import os
import re
from flask import Flask, render_template, request, send_file
import conf

app = Flask(__name__)

def group_files(path, file_list):
    dirs = []
    files = []

    for f in file_list:
        if os.path.isdir(path + f):
            dirs.append(['dir', f, 0])
        else:
            files.append(['file', f, os.path.getsize(path+f)])

    dirs.sort()
    files.sort()
    return dirs + files

@app.route('/')
def index():
    """ Empty path gives 404 so we need a separate endpoint for home """
    resources = conf.BaseConfig.FILES_BASE_PATH
    file_list = os.listdir(resources)
    file_list = group_files(resources, file_list)
    return render_template('index.html', files=file_list, path='')

@app.route('/<path:path>')
def file_path(path):
    """ Take an arbitrary path and return the files or file """
    resources = conf.BaseConfig.FILES_BASE_PATH
    print(path)
    print(os.path.isdir(resources+path))
    if os.path.isdir(resources+path):
        file_list = os.listdir(resources+path)
        file_list = group_files(file_list)
        return render_template('index.html', files=file_list, path=path)

    return send_file(resources+path)
