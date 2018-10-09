import unittest
from modules import helpers

class TestHelperMethods(unittest.TestCase):

    def test_no_score(self):
        self.assertEqual(helpers.checkScore([6,6,2,3,4]), 0)


if __name__ == '__main__':
    unittest.main()