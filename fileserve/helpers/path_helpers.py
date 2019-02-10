""" Helper functions for file paths """

def ensure_trailing_slash(path):
    """ Ensure a given path contains a trailing slash """
    print(path)
    if not path.endswith('/'):
        return path + '/'
    return path
