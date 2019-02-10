""" Unit test helper methods """

import unittest
from fileserve import helpers

class TestHelperMethods(unittest.TestCase):
    """ Class representing test case """
    def test_ensure_trailing_slash(self):
        """ Test trailing slash works """
        trailing_slash = '/my/path/with/shash/'
        no_trailing_slash = '/my/path/with/no/slash'
        expected_no_slash = no_trailing_slash + '/'
        expected_trailing_slash = trailing_slash

        actual_no_slash = helpers.path_helpers.ensure_trailing_slash(no_trailing_slash)
        actual_slash = helpers.path_helpers.ensure_trailing_slash(trailing_slash)

        self.assertEqual(actual_no_slash, expected_no_slash)
        self.assertEqual(actual_slash, expected_trailing_slash)

    def test_join_paths(self):
        """ Test join paths function works """
        paths = ['/this/is', '/my/path', 'and/such/']
        expected = '/this/is/my/path/and/such/'
        actual = helpers.path_helpers.join_paths(paths)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
