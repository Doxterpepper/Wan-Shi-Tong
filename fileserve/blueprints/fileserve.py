""" Define controller """

import os
from flask import Blueprint, render_template, send_file, session, redirect, url_for
from .. import conf
from .. import filemodel

api = Blueprint('fileserve', __name__, url_prefix='/')

@api.route('/')
def index():
    """ Empty path gives 404 so we need a separate endpoint for home """
    if 'username' not in session:
        return redirect(url_for('auth_controller.login'))

    filemodel_list = filemodel.filelist.FileList('/')
    return render_template('index.html', files=filemodel_list)

@api.route('/<path:path>')
def file_path(path):
    """ Take an arbitrary path and return the files or file """
    if 'username' not in session:
        return redirect(url_for('auth_controller.login'))
    fileserve_source = conf.BaseConfig.FILES_BASE_PATH
    if os.path.isdir(fileserve_source + path):
        filemodel_list = filemodel.filelist.FileList(path)
        return render_template('index.html', files=filemodel_list)
    return send_file(fileserve_source + path)
