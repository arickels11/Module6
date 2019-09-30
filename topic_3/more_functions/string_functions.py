"""CIS 189
Alex Rickels
Module 6 Topic 3 Assignment 2 """


def multiple_string(statement, n):  # function
    """ 
    :param statement: the statement to be printed n determined number of times
    :param n: the number of times the statement will be printed
    :returns string of 'statement' printed 'n' times"""  # docstring
    return statement * n


if __name__ == '__main__':  # function call
    multiple_string("Yo", 4)
