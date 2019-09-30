import unittest
from topic_3.more_functions import string_functions

class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(YoYoYoYo, string_functions.multiple_string("Yo", 4))


if __name__ == '__main__':
    unittest.main()
