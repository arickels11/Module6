"""CIS 189
Alex Rickels
Module 6 Topic 4 Assignment"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: mandatory input, name of the test
    :param test_score: optional input, score the user received on the test
    :param invalid_message: optional input, message received if score input is not between 0 and 100
    :return: the test name and the valid test score"""

    if test_score in range(0, 100):
        return test_name + ": " + str(test_score)
    else:
        return invalid_message


if __name__ == '__main__':
    print(score_input("main test", -20, "WRONG"))
