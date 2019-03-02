""" Tests login integration """

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginIntegration(unittest.TestCase):
    """ Test class for testing login """

    def setUp(self):
        ''' setup selenium '''
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:5501')

    def tearDown(self):
        """ Tear down selenium """
        self.driver.close()

    def test_login(self):
        """ Test login """
        self.driver.find_element(By.NAME, 'username').send_keys('dock')
        self.driver.find_element(By.NAME, 'password').send_keys('password1!')
        self.driver.find_element(By.CSS_SELECTOR, '.btn').click()
        self.driver.find_element_by_link_text('Logout')

    def test_logout(self):
        """ test logout functionaility """
        self.test_login()
        self.driver.find_element_by_link_text('Logout').click()
        self.driver.find_element(By.NAME, 'username')

    def test_invalid_login(self):
        """ test invalid login credentials prevents login """
        login_credentials = [
            ('invalid', 'password1!'),
            ('dock', 'invalid'),
        ]
        for username, password in login_credentials:
            self.driver.find_element(By.NAME, 'username').send_keys(username)
            self.driver.find_element(By.NAME, 'password').send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, '.btn').click()
            self.assertTrue('Invalid username or password' in self.driver.page_source)
        # test we can still login after failures
        self.test_login()

    def test_login_redirects(self):
        """ Test different redirects take you to login page """
        redirects = [
            '/generate-url',
            '/register',
            '/register/99999999999999999/',
            '/',
            '/test'
        ]

        for page in redirects:
            self.driver.get('http://localhost:5501' + page)
            self.assertEqual(self.driver.current_url, 'http://localhost:5501/login')
