""" Handles interfacing with the database for users """

from ..user_model.user_model import User

class UserDataHandler:
    """ User data handler """
    def __init__(self, db):
        """ Intitialize the datahandler with the database connection """
        self.db = db

    def get_user_password(self, username):
        """ Select password from database using username and return a User object """
        connection = self.db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT Password FROM Users WHERE Username = %s', [username])
            result = cursor.fetchone()
            if result is None:
                return None

            password = result[0]
            return User(username, password)
