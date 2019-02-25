""" Registration endpoints """

from flask import Blueprint, redirect, session, url_for, render_template, request
from .. import dependency_resolver
from ..models.user_model import User
from ..helpers.view_helpers import require_auth
from ..exceptions.invalid_user import InvalidUserException
from ..exceptions.invalid_input import InvalidInputException

user_business = dependency_resolver.resolve('UserBusiness')
registration_business = dependency_resolver.resolve('RegistrationBusiness')

reg_endpoint = Blueprint('registration', __name__, url_prefix='/registration')


@reg_endpoint.route('/generate-url', methods=['GET'])
@require_auth
def generate_url():
    """ Generate a invite page """
    # Must be admin, otherwise go to the index
    if not user_business.is_admin(session['username']):
        return redirect(url_for('fileserve.index'))

    code = registration_business.generate_code()
    return render_template('invite.html', url=request.url_root[:-1], invite_code=code)

@reg_endpoint.route('/register/<code>', methods=['GET'])
def register(code):
    """ Registration page with code """
    if not registration_business.check_registration_code(code):
        return redirect(url_for('auth_controller.login'))

    return render_template('register.html', invite_code=code)

@reg_endpoint.route('/register/<code>', methods=['POST'])
def create_account(code):
    """ Create an account """
    if not registration_business.check_registration_code(code):
        return redirect(url_for('auth_controller.login'))

    try:
        username, password = validate_create(request.form, code)
    except InvalidInputException as e:
        return render_template('register.html', invite_code=code, error=e.message)

    try:
        user_business.save(username, password)
    except InvalidUserException as e:
        return render_template('register.html', invite_code=code, error=e.message)

    session['username'] = username

    return redirect(url_for('fileserve.index'))

def validate_create(form, code):
    required = ['username', 'password', 're-password']
    for param in required:
        if not param in request.form or not form[param]:
            raise InvalidInputException('Must include field: ' + param)

    username = request.form['username']
    password = request.form['password']
    re_password = request.form['re-password']

    if password != re_password:
            raise InvalidInputException('Passwords do not match')

    return (username, password)

