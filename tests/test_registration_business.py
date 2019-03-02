""" Registration business tests """

import datetime
from unittest.mock import MagicMock
import unittest
from fileserve.business.registration_business import RegistrationBusiness
from fileserve.conf import BaseConfig

class TestRegistrationBusiness(unittest.TestCase):
    """ Test cases for registration business """

    def test_generate_code(self):
        """ Test the generate_code method """
        # Arrange
        mock_data_handler = MagicMock()
        user_business = RegistrationBusiness()
        user_business.registration_datahandler = mock_data_handler

        # Act
        token = user_business.generate_code()

        # Assert
        mock_data_handler.save_code.assert_called_once()
        self.assertTrue(len(token) > 0)

    def test_check_registration_code(self):
        """ Test the check_registration_code method """
        # Arrange
        BaseConfig.CODE_TIMEOUT = datetime.timedelta(hours=3)
        delta = datetime.timedelta(hours=2)
        time_stamp = datetime.datetime.utcnow() - delta

        mock_data_handler = MagicMock()
        mock_data_handler.retrieve_time_stamp.return_value = time_stamp
        user_business = RegistrationBusiness()
        user_business.registration_datahandler = mock_data_handler
        valid = user_business.check_registration_code('')

        self.assertTrue(valid)

    def test_check_registration_code_fails(self):
        """ Test negative test case for check_registration_code method """
        BaseConfig.CODE_TIMEOUT = datetime.timedelta(hours=3)
        delta = datetime.timedelta(hours=4)
        time_stamp = datetime.datetime.utcnow() - delta

        mock_data_handler = MagicMock()
        mock_data_handler.retrieve_time_stamp.return_value = time_stamp
        user_business = RegistrationBusiness()
        user_business.registration_datahandler = mock_data_handler
        valid = user_business.check_registration_code('')

        self.assertFalse(valid)

    def test_check_registration_code_failse_with_none(self):
        """ Test negative test case when time_stamp is none """
        BaseConfig.CODE_TIMEOUT = datetime.timedelta(hours=3)
        time_stamp = None

        mock_data_handler = MagicMock()
        mock_data_handler.retrieve_time_stamp.return_value = time_stamp
        user_business = RegistrationBusiness()
        user_business.registration_datahandler = mock_data_handler
        valid = user_business.check_registration_code('')

        self.assertFalse(valid)
