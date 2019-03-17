""" Database methods """

import psycopg2
from .conf import BaseConfig

class BaseDatabase:
    """ Database wrapper """

    connection = None

    def get_connection(self):
        """ method to get database object. Creates the object on first call """
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=BaseConfig.DATABASE_NAME,
                user=BaseConfig.DATABASE_USER,
                host=BaseConfig.DATABASE_HOST
            )

        return self.connection
