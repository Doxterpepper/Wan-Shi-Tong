""" Test registration """

import re
import secrets
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestRegistration(unittest.TestCase):
    """ Test class for registration """

    def setUp(self):
        ''' setup selenium '''
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:5501')

    def tearDown(self):
        """ Tear down selenium """
        self.driver.close()

    def admin_login(self):
        """ Test login """
        self.driver.find_element(By.NAME, 'username').send_keys('dock')
        self.driver.find_element(By.NAME, 'password').send_keys('password1!')
        self.driver.find_element(By.CSS_SELECTOR, '.btn').click()
        self.driver.find_element_by_link_text('Logout')

    def logout(self):
        """ Logout """
        self.driver.find_element_by_link_text('Logout').click()

    def test_generate_register_link(self):
        """ Test generating the registration link """
        self.admin_login()
        self.driver.find_element_by_link_text('Invite').click()
        link_box = self.driver.find_element(By.CSS_SELECTOR, '.container input')
        link = link_box.get_attribute('value')
        match_string = '^http://localhost:5501/registration/register/.{22}'
        self.assertTrue(re.match(match_string, link))

    def test_register(self):
        """ test registration works """
        self.test_generate_register_link()
        link_box = self.driver.find_element(By.CSS_SELECTOR, '.container input')
        link = link_box.get_attribute('value')
        self.logout()
        self.driver.get(link)
        username = secrets.token_urlsafe()
        # random username
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys('testpassword1!')
        self.driver.find_element(By.NAME, 're-password').send_keys('testpassword1!')
        self.driver.find_element(By.CSS_SELECTOR, '.btn').click()
        self.driver.find_element_by_link_text('Logout')
        # New user should not be admin
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text('Invite')
