"""CIS 189
Alex Rickels
Module 6 Topic 4 Assignment"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: mandatory input, name of the test
    :param test_score: optional input, score the user received on the test
    :param invalid_message: optional input, message received if score input is not between 0 and 100
    :return: the test name and the valid test score
    """
    pass
    # while True:
    #     try:
    #         test_score = int(input("What was your test score?"))
    #     except ValueError:
    #         print(invalid_message)
    #     if 0 >= test_score:
    #         return True
    #     if 100 <= test_score:
    #         return True

    # return {test_name: test_score}


if __name__ == '__main__':
    score_input("pasta type test")
