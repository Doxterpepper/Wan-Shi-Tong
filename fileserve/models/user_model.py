""" Model for users """

class User:
    """ Class to represent users """
    def __init__(self, username, password=None):
        """ Initialize a user """
        self.username = username
        self.password = password
