""" Define controller """

import os
from flask import Blueprint, render_template, send_file, session
from ..helpers.view_helpers import require_auth
from .. import conf
from ..models.filelist import FileList
from .. import dependency_resolver
from ..helpers import path_helpers

user_business = dependency_resolver.resolve('UserBusiness')

api = Blueprint('fileserve', __name__, url_prefix='/')

@api.route('/')
@require_auth
def index():
    """ Empty path gives 404 so we need a separate endpoint for home """
    username = session['username']
    is_admin = user_business.is_admin(username)

    filemodel_list = FileList('/')
    return render_template('index.html', files=filemodel_list, is_admin=is_admin)

@api.route('/<path:path>')
@require_auth
def file_path(path):
    """ Take an arbitrary path and return the files or file """
    fileserve_source = path_helpers.ensure_trailing_slash(conf.BaseConfig.FILES_BASE_PATH)
    username = session['username']
    is_admin = user_business.is_admin(username)

    if os.path.isdir(fileserve_source + path):
        filemodel_list = FileList(path)
        return render_template('index.html', files=filemodel_list, is_admin=is_admin)
    return send_file(fileserve_source + path)
