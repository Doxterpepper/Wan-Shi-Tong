""" Define user auth controller """

from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, session, request
from ..helpers import view_helpers
from .. import dependency_resolver
from ..conf import BaseConfig

temp_ban = {}

user_business = dependency_resolver.resolve('UserBusiness')

controller = Blueprint('auth_controller', __name__, url_prefix='/')

@controller.route('/login', methods=['GET'])
def login():
    """ Render login page """
    if view_helpers.is_authorized():
        return redirect(url_for('fileserve.index'))

    return render_template('login.html')

@controller.route('/login', methods=['POST'])
def login_post():
    """ Login """
    is_banned = is_temp_ban(request.remote_addr)
    if is_banned or 'retries' in session and session['retries'] > BaseConfig.MAX_LOGIN_RETRIES:
        return render_template('login.html', error='Too many retries, try agian later')

    if not 'username' in request.form or not 'password' in request.form:
        return render_template('login.html', error='Username and Password fields required')

    username = request.form['username']
    password = request.form['password']

    if not user_business.validate(username, password):
        if 'retries' in session:
            session['retries'] += 1
        else:
            session['retries'] = 1

        if session['retries'] > 4:
            temp_ban[request.remote_addr] = datetime.utcnow()
            session['retries'] = 0

        return render_template('login.html', error='Invalid username or password')

    session['username'] = username
    session['timestamp'] = datetime.utcnow()

    return redirect(url_for('fileserve.index'))

def is_temp_ban(ip_addr):
    """ Check ip address for temp ban """
    if ip_addr in temp_ban:
        return datetime.utcnow() - temp_ban[ip_addr] < BaseConfig.BAN_TIMEOUT
    return False

@controller.route('/logout')
def logout():
    """ Logout """
    session.pop('username', None)
    session.pop('timestamp', None)
    return redirect(url_for('auth_controller.login'))
