""" Model for users """

class User:
    """ Class to represent users """
    def __init__(self, username, password=None, user_level=0):
        """ Initialize a user """
        self.username = username
        self.password = password
        self.user_level = user_level
