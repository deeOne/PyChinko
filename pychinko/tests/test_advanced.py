from .context import core

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(core.hmm())

if __name__ == '__main__':
    unittest.main()