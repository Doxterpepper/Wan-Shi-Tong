""" User business """

import bcrypt
from ..models.user_model import User

class UserBusiness:
    """ User business class """
    user_datahandler = None

    def validate(self, username, password):
        """ Check if username and password are valid """
        user = self.user_datahandler.get_user(username)
        if user is None:
            return False

        # User password is expected to be hashed.
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def is_admin(self, username):
        """ Check if the user is administrator """
        user = self.user_datahandler.get_user(username)
        return user.user_level > 0

    def save(self, username, password):
        """ Save the user """
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User(username, hashed_password.decode())
        self.user_datahandler.save_user(user)
