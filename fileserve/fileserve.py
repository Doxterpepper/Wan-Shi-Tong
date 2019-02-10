""" Simple flask app for serving static files """

from flask import Flask
from . import conf

__all__ = ['create_app']

def create_app():
    """ Create the flask app """
    app_name = conf.BaseConfig.PROJECT
    template_folder = conf.BaseConfig.PROJECT_ROOT + '/templates'
    static_folder = conf.BaseConfig.PROJECT_ROOT + '/static'

    app = Flask(app_name, template_folder=template_folder, static_folder=static_folder)
    configure_blueprints(app)
    return app

def configure_blueprints(app):
    """ Configurate blueprints for flask app """
    from . import fileserve_controller

    app.register_blueprint(fileserve_controller.controller.api)
