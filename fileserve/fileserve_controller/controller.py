""" Define controller """

import os
from flask import Blueprint, render_template, send_file
from .. import conf
from .. import filemodel

api = Blueprint('fileserve_controller', __name__, url_prefix='/')

@api.route('/')
def index():
    """ Empty path gives 404 so we need a separate endpoint for home """
    filemodel_list = filemodel.filelist.FileList('/')
    return render_template('index.html', files=filemodel_list)

@api.route('/<path:path>')
def file_path(path):
    """ Take an arbitrary path and return the files or file """
    fileserve_source = conf.BaseConfig.FILES_BASE_PATH
    if os.path.isdir(fileserve_source + path):
        filemodel_list = filemodel.filelist.FileList(path)
        return render_template('index.html', files=filemodel_list)
    return send_file(fileserve_source + path)
