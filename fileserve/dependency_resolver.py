""" Dependency resolving methods """

from .database import BaseDatabase
from .data_handlers.user_datahandler import UserDataHandler
from .business.user_business import UserBusiness

# Here we maintan a table of dependencies and what they resolve to.
registration_table = {
    'db': BaseDatabase,
    'user_datahandler': UserDataHandler,
    'UserBusiness': UserBusiness
}

def resolve(dependency):
    """ Resolve the dependency by name and recusively resolve it's dependencies """
    dep = registration_table[dependency]

    # Go through attributes and fill in the ones that are registered
    for attr in dir(dep):
        if attr in registration_table:
            setattr(dep, attr, resolve(attr))

    # Actually call constructor
    return dep()
