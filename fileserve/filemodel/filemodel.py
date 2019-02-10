""" Model to represent a given file """

import os
from .. import icon_registry

class FileModel:
    """ Represents a file, will track size, file type ect """

    def __init__(self, source_folder, path, name):
        """ Constructs a file model """
        self.path = path
        self.name = name
        self.full_path = path + name
        self.isdir = os.path.isdir(source_folder + self.full_path)
        if self.isdir:
            self.size = ''
        else:
            self.size = os.path.getsize(source_folder + self.full_path)

        self.icon = get_file_icon(self.name)

def build_filemodel_list(source_folder, path):
    """ Takes a list of files and builds a list of FileModels """
    dirs = []
    file_list = []

    path += '/'

    # Group files based on directories and files
    files = os.listdir(source_folder + path)
    for f in files:
        if os.path.isdir(source_folder + path + f):
            dirs.append(FileModel(source_folder, path, f))
        else:
            file_list.append(FileModel(source_folder, path, f))

    # Sort the files on their file name
    dirs.sort(key=lambda x: x.name)
    file_list.sort(key=lambda x: x.name)

    # Dirs should be on top of the files
    return dirs + file_list

def get_file_icon(path):
    """ Get the file extension """
    if os.path.isdir(path):
        return icon_registry.directory_icon

    extension = path.split('.')[-1]

    if extension in icon_registry.registry:
        return icon_registry.registry[extension]

    return icon_registry.base_file_icon
