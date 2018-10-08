import unittest
from modules import helpers

class TestHelperMethods(unittest.TestCase):

    def test_no_score(self):
        self.assertEqual(helpers.checkScore([6,6,2,3,4]), 0)

    def test_array_too_long(self):
        self.assertEqual(helpers.checkScore([6,6,2,3,4]).exception.code, 1)

if __name__ == '__main__':
    unittest.main()