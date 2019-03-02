""" Define user auth controller """

from flask import Blueprint, render_template, redirect, url_for, session, request
from .. import dependency_resolver

user_business = dependency_resolver.resolve('UserBusiness')

controller = Blueprint('auth_controller', __name__, url_prefix='/')

@controller.route('/login', methods=['GET'])
def login():
    """ Render login page """
    if 'username' in session:
        return redirect(url_for('fileserve.index'))

    return render_template('login.html')

@controller.route('/login', methods=['POST'])
def login_post():
    """ Login """
    if not 'username' in request.form or not 'password' in request.form:
        return render_template('login.html', error='Username and Password fields required')

    username = request.form['username']
    password = request.form['password']

    if not user_business.validate(username, password):
        return render_template('login.html', error='Invalid username or password')

    session['username'] = username

    return redirect(url_for('fileserve.index'))

@controller.route('/logout')
def logout():
    """ Logout """
    session.pop('username', None)
    return redirect(url_for('auth_controller.login'))
