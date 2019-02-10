""" Simple flask app for serving static files """

from flask import Flask
from . import conf

__all__ = ['create_app']

def create_app():
    """ Create the flask app """
    app_name = conf.BaseConfig.PROJECT

    app = Flask(app_name)
    configure_blueprints(app)
    return app

def configure_blueprints(app):
    """ Configurate blueprints for flask app """
    from . import fileserve_controller

    app.register_blueprint(fileserve_controller.controller.api)
