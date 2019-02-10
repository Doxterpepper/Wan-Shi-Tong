""" Model to represent a given file """

import os
from .. import icon_registry
from .. import conf
from ..helpers import path_helpers

class FileModel:
    """ Represents a file, will track size, file type ect """

    def __init__(self, path, name):
        """ Constructs a file model """
        self.path = path_helpers.ensure_trailing_slash(path)
        self.name = name
        full_path = path_helpers.join_paths([path, name])
        base_path = conf.BaseConfig.FILES_BASE_PATH
        if conf.BaseConfig.VIRTUAL_PATH == '':
            self.href = full_path
        else:
            self.href = path_helpers.join_paths([conf.BaseConfig.VIRTUAL_PATH, full_path])

        self.isdir = os.path.isdir(path_helpers.join_paths([base_path, full_path]))
        if self.isdir:
            self.size = ''
        else:
            self.size = os.path.getsize(path_helpers.join_paths([base_path, full_path]))

        self.icon = self.get_file_icon()

    def get_file_icon(self):
        """ Get the file extension """
        if self.isdir:
            return icon_registry.directory_icon

        extension = self.name.split('.')[-1]

        if extension in icon_registry.registry:
            return icon_registry.registry[extension]

        return icon_registry.base_file_icon
