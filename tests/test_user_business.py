""" Test user business """

from unittest.mock import MagicMock
import unittest
import bcrypt
from fileserve import business
from fileserve.models.user_model import User

class TestUserBusiness(unittest.TestCase):
    """ Test cases for user business logic """

    def test_validate(self):
        """ Test the validate method """
        user_table = [
            ('testusername', 'password1!', 'password1!', True),
            ('testusername', 'password1!', 'password10', False),
        ]

        for username, password, expectedpw, authenticated in user_table:
            # Password retrieved will be a decoded password as a string
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(expectedpw.encode(), salt).decode()
            user = User(username, hashed_password)

            mock_data_handler = MagicMock()
            mock_data_handler.get_user.return_value = user

            user_business = business.user_business.UserBusiness()
            user_business.user_datahandler = mock_data_handler

            # Act
            is_valid = user_business.validate(username, password)

            # Assert
            self.assertEqual(is_valid, authenticated)

    def test_is_admin(self):
        """ Test is_admin method """
        admin_table = [
            (1, True), # Is admin
            (10, True), # Is admin
            (0, False), # Not admin
        ]

        for user_level, admin in admin_table:
            # Arrange
            user = User('username', 'irrelavant password', user_level)
            mock_data_handler = MagicMock()
            mock_data_handler.get_user.return_value = user
            user_business = business.user_business.UserBusiness()
            user_business.user_datahandler = mock_data_handler

            # Act
            is_admin = user_business.is_admin('username')

            # Assert
            self.assertEqual(is_admin, admin)

    def test_save(self):
        """ Test the save method """
        username = 'username'
        password = 'password1!'
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        mock_data_handler = MagicMock()
        correct_hash = None
        user_business = business.user_business.UserBusiness()
        user_business.user_datahandler = mock_data_handler

        user_business.save('test_username', 'test_password')
        mock_data_handler.save_user.assert_called_once()

if __name__ == '__main__':
    unittest.main()

