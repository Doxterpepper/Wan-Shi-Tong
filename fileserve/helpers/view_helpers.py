""" View decorators """

from datetime import datetime
from functools import wraps
from flask import redirect, url_for, session
from ..conf import BaseConfig

def require_auth(view_func):
    """ Define decorator for require authentication """
    def _decorator(*args, **kwargs):
        if is_authorized():
            return view_func(*args, **kwargs)
        return redirect(url_for('auth_controller.login'))
    return wraps(view_func)(_decorator)

def is_authorized():
    """ Check if user is authorized """
    return 'username' in session and 'timestamp' in session and check_timeout()

def check_timeout():
    """ Checks timeout on session"""
    return datetime.utcnow() - session['timestamp'] < BaseConfig.SESSION_TIMEOUT
