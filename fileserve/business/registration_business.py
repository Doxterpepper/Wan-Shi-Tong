""" Registration business """

from datetime import datetime
import secrets

from ..conf import BaseConfig

class RegistrationBusiness:
    """ Class for regisration business """

    registration_datahandler = None

    def generate_code(self):
        """ Generate the regisration page code """
        token = secrets.token_urlsafe(16)
        time_stamp = datetime.utcnow()
        self.registration_datahandler.save_code(token, time_stamp)
        return token

    def check_registration_code(self, code):
        """ Check timestamp on registration code """
        time_stamp = self.registration_datahandler.retrieve_time_stamp(code)
        if time_stamp is None:
            return False

        return datetime.utcnow() - time_stamp <= BaseConfig.CODE_TIMEOUT
