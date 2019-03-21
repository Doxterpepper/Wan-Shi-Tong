import psycopg2

db = psycopg2.connect(
    dbname='WanShiTong',
    user='admin',
    host='localhost'
)

with db.cursor() as cursor:
    print('Creating Users')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users 
        (
            Username      TEXT        PRIMARY KEY,
            Password      TEXT,
            UserLevel     NUMERIC     DEFAULT 0
        );
    ''')

    print('Creating RegistrationCodes')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RegistrationCodes
        (
            Code          TEXT,
            TimeStamp     TEXT
        );
    ''')

db.commit()
