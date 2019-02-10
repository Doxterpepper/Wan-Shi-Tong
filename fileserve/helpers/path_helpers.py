""" Helper functions for file paths """

import re

def ensure_trailing_slash(path):
    """ Ensure a given path contains a trailing slash """
    print(path)
    if not path.endswith('/'):
        return path + '/'
    return path

def join_paths(paths):
    """ Join paths and remove repeating slashes """
    joined = '/'.join(paths)
    return re.sub('//+', '/', joined)
