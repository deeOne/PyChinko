# -*- coding: utf-8 -*-
from .context import pychinko

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    print('this worked')

    def test_absolute_truth_and_meaning(self):
        assert True

if __name__ == '__main__':
    unittest.main()