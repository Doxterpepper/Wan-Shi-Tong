""" Database methods """

import bcrypt
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

def deploy():
    """ Deploy the database tables """
    db = BaseDatabase().get_connection()
    with db.cursor() as cursor:
        print('attempting create table users')
        cursor.execute('''
            DROP TABLE Users;
            CREATE TABLE IF NOT EXISTS USERS 
            (
                Username      TEXT        PRIMARY KEY,
                Password      TEXT,
                UserLevel     NUMERIC     DEFAULT 0
            );
        ''')

        default_username = 'dock'
        default_password = bcrypt.hashpw('password1!'.encode(), bcrypt.gensalt())
        cursor.execute('''
            INSERT INTO Users
            (
                Username,
                Password,
                UserLevel
            )
            VALUES (%s, %s, %s);
        ''', [default_username, default_password.decode(), 1])

        print('attempting to create registration code table')
        cursor.execute('''
            DROP TABLE RegistrationCodes;
            CREATE TABLE IF NOT EXISTS RegistrationCodes
            (
                Code          TEXT,
                TimeStamp     TEXT
            );
        ''')
        db.commit()
