""" Datahandler for registration links """

from datetime import datetime

class RegistrationDataHandler:
    """ Class for registration data handling """

    db = None

    def save_code(self, code, time_stamp):
        """ save the code and time stamp in the DB """
        connection = self.db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO RegistrationCodes
                VALUES (%s, %s);
            ''', [code, str(time_stamp)])
        connection.commit()

    def retrieve_time_stamp(self, code):
        """ Get the time stamp of a given code """
        connection = self.db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT TimeStamp
                FROM RegistrationCodes
                WHERE Code = %s;
            ''', [code])

            result = cursor.fetchone()
            if result is None:
                return None

            timestamp = result[0]
            time_format = '%Y-%m-%d %H:%M:%S.%f'

            return datetime.strptime(timestamp, time_format)
