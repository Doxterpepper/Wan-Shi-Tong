""" Test user business """

from unittest.mock import MagicMock
import unittest
import bcrypt
from fileserve import business
from fileserve.user_model.user_model import User

class TestUserBusiness(unittest.TestCase):
    """ Test cases for user business logic """

    def test_validate(self):
        """ Test the validate method """
        # Arrange
        username = 'testusername'
        password = 'password1!'

        # Password retrieved will be a decoded password as a string
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(username, hashed_password)

        mock_data_handler = MagicMock()
        mock_data_handler.get_user_password.return_value = user

        user_business = business.user_business.UserBusiness(mock_data_handler)

        # Act
        is_valid = user_business.validate(username, password)

        # Assert
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()
