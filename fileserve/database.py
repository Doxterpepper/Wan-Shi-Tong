""" Database methods """

import psycopg2
from .conf import BaseConfig

db = psycopg2.connect(dbname='WanShiTong', user='admin', host='localhost')

def deploy():
    """ Deploy the database tables """
    with db.cursor() as cursor:
        print('attempting create table users')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS 
            (
                Username TEXT,
                Password TEXT
            );
        ''')
        db.commit()
