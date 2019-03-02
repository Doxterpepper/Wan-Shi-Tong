""" Collection of basic tasks """

from invoke import task

@task
def test(c):
    """ Run unit tests """
    c.run('python -m unittest tests/*.py')

@task
def integration(c):
    """ Run integration tests """
    c.run('python -m unittest integration_tests/*.py')

@task
def lint(c):
    """ Run pylint """
    c.run('pylint fileserve tests')

@task
def debug(c):
    """ Run project with flask in debug mode """
    c.run('FLASK_APP=wsgi_app.py FLASK_DEBUG=True flask run -p 5501')
