""" View decorators """

from functools import wraps
from flask import redirect, url_for, session

def require_auth(view_func):
    """ Define decorator for require authentication """
    def _decorator(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('auth_controller.login'))
        return view_func(*args, **kwargs)
    return wraps(view_func)(_decorator)
