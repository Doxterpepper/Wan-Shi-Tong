""" Define user auth controller """

controller = Blueprint('auth_controller', __name__, url_prefix='/')

@api.route('/login')
def login():
    """ Render login page """
    return render_template('login.html')
