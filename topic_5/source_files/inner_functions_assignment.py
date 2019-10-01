"""CIS 189
Alex Rickels
Module 6 Topic 5 Assignment"""


def measurements(rec_list):
    def area():
        return float(rec_list[0] * rec_list[1])

    def perimeter():
        return float((rec_list[0] * 2) + (rec_list[1] * 2))
    return "Perimeter = " + str(perimeter()) + " Area = " + str(area())


if __name__ == '__main__':
    print(measurements([2, 3]))
