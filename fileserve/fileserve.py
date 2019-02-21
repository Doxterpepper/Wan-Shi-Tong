""" Simple flask app for serving static files """

from flask import Flask
from . import conf
from . import database

__all__ = ['create_app']

def create_app():
    """ Create the flask app """
    app_name = conf.BaseConfig.PROJECT
    template_folder = conf.BaseConfig.PROJECT_ROOT + '/templates'
    static_folder = conf.BaseConfig.PROJECT_ROOT + '/static'

    app = Flask(app_name, template_folder=template_folder, static_folder=static_folder)
    app.secret_key = b'0asdfi8%2!o19283h'
    configure_database()
    configure_blueprints(app)
    return app

def configure_blueprints(app):
    """ Configurate blueprints for flask app """
    from . import blueprints

    app.register_blueprint(blueprints.fileserve.api)
    app.register_blueprint(blueprints.user_auth.controller)

def configure_database():
    """ Configure Ensure database tables are present """
    database.deploy()
