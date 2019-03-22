""" Config file for plant_tracker """

import os
from datetime import timedelta

class BaseConfig():
    """ Base config for plant tracker """
    PROJECT = 'dock_fileshare'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    FILES_BASE_PATH = PROJECT_ROOT + '/rec/'
    STATIC_FILES = 'static'
    VIRTUAL_PATH = ''
    DATABASE_NAME = 'WanShiTong'
    DATABASE_USER = 'admin'
    DATABASE_HOST = 'localhost'
    DATABASE_PASSWORD = None

    DEBUG = False
    TESTING = False

    CODE_TIMEOUT = timedelta(hours=3)
    SESSION_TIMEOUT = timedelta(minutes=5)

    ADMINS = ['mail@dockoneal.com']

    SECRET_KEY = ''
