""" User business """

import bcrypt

class UserBusiness:
    """ User business class """
    user_datahandler = None

    def validate(self, username, password):
        """ Check if username and password are valid """
        user = self.user_datahandler.get_user_password(username)
        if user is None:
            return False

        # User password is expected to be hashed.
        return bcrypt.checkpw(password.encode(), user.password.encode())
