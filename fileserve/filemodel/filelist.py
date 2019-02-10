""" Defines class representing a list of file models  """

import os
from .. import conf
from . import filemodel
from ..helpers import path_helpers

class FileList:
    """ Model representing a list of files """
    def __init__(self, path):
        """ Constructes a direcotry model including a list of all files as filemodels """
        # path must have a trailing '/'
        path = path_helpers.ensure_trailing_slash(path)

        self.path = path
        self.files = self.get_files()

    def get_files(self):
        """ Gets all files in the path """
        full_path = path_helpers.join_paths([conf.BaseConfig.FILES_BASE_PATH, self.path])
        dirs = []
        files = []


        # Group files as directories and regular files
        for f in os.listdir(full_path):
            model = filemodel.FileModel(self.path, f)
            if model.isdir:
                dirs.append(model)
            else:
                files.append(model)

        # Sort files by name
        dirs.sort(key=lambda x: x.name)
        files.sort(key=lambda x: x.name)

        # directories should come before files
        return dirs + files
