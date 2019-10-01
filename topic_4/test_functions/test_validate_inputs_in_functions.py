import unittest
from topic_4.more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Pasta test: 0", validate_input_in_functions.score_input("Pasta test"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Soup test: 88", validate_input_in_functions.score_input("Soup test", 88))

    def test_score_input_test_score_below_range(self):
        self.assertEqual('Invalid test score, try again!', validate_input_in_functions.score_input("Veggie test", -10))

    def test_score_input_test_score_above_range(self):
        self.assertEqual('Invalid test score, try again!', validate_input_in_functions.score_input("Fruit test", 200))

    def test_test_score_non_numeric(self):
        self.assertEqual('Invalid test score, try again!', validate_input_in_functions.score_input("alpha test", "a"))

    def test_score_input_invalid_message(self):
        self.assertEqual("TRY AGAIN", validate_input_in_functions.score_input("final test", 120, "TRY AGAIN"))


if __name__ == '__main__':
    unittest.main()
