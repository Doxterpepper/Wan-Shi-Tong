""" User queries """

class UserQueries:
    """ Class of user SQL queries """

    select_username = '''
        SELECT Username
        FROM Users
        WHERE Username=%s;
    '''

    insert_user = '''
        INSERT INTO Users
        (
            Username,
            Password,
            UserLevel
        )
        VALUES (%s, %s, %s)
    '''

    select_password_userlevel = '''
        SELECT Password, UserLevel 
        FROM Users 
        WHERE Username = %s
    '''
