""" Handles interfacing with the database for users """

from ..models.user_model import User
from ..exceptions.invalid_user import InvalidUserException

class UserDataHandler:
    """ User data handler """
    db = None

    def get_user(self, username):
        """ Select password from database using username and return a User object """
        connection = self.db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT Password, UserLevel 
                FROM Users 
                WHERE Username = %s
            ''', [username])

            result = cursor.fetchone()
            if result is None:
                return None

            password, user_level = result
            return User(username, password, user_level)

    def save_user(self, user):
        """ Saves a user model """
        connection = self.db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT Username
                FROM Users
                WHERE Username=%s;
            ''', [user.username])

            if cursor.fetchone() is not None:
                raise InvalidUserException('User already exists')

            cursor.execute('''
                INSERT INTO Users
                (
                    Username,
                    Password,
                    UserLevel
                )
                VALUES (%s, %s, %s)
            ''', [user.username, user.password, user.user_level])
        connection.commit()
        return True
