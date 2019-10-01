"""CIS 189
Alex Rickels
Module 6 Topic 5 Assignment"""


def measurements(rec_list):  # outer function
    """
    :param rec_list: variable list of length and width of rectangle, or length of a square
    :return: area and perimeter of the rectangle
    """

    def area():  # inner function
        if len(rec_list) == 2:
            return float(rec_list[0] * rec_list[1])
        elif len(rec_list) == 1:
            return float(rec_list[0] * rec_list[0])

    def perimeter():  # inner function
        if len(rec_list) == 2:
            return float((rec_list[0] * 2) + (rec_list[1] * 2))
        elif len(rec_list) == 1:
            return float(rec_list[0] * 4)

    return "Perimeter = " + str(perimeter()) + " Area = " + str(area())


if __name__ == '__main__':
    print(measurements([2]))
