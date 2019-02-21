""" Test filelist """

import unittest
import mock
from fileserve import filemodel

class TestFileList(unittest.TestCase):
    """ Test the FileList class """
    @mock.patch('fileserve.filemodel.filelist.os.path.isdir')
    @mock.patch('fileserve.filemodel.filelist.os.listdir')
    def test_create(self, mock_listdir, mock_isdir):
        """ Test creation of FileList """
        path = '/srv/test'
        directory_content = [
            ''
        ]
        filemodel.filelist.FileList(path)

if __name__ == '__main__':
    unittest.main()
