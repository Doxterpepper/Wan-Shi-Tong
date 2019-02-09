""" Config file for plant_tracker """

import os

class BaseConfig():
    """ Base config for plant tracker """
    PROJECT = 'dock_fileshare'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    FILES_BASE_PATH = PROJECT_ROOT + '/rec/'

    DEBUG = False
    TESTING = False

    ADMINS = ['mail@dockoneal.com']

    SECRET_KEY = ''
