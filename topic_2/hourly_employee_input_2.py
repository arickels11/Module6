"""CIS 189
Alex Rickels
Topic 2 Assignment 1"""


def hourly_employee_input():
    """this function gets user input for name, hours, and hourly rate and prints name and calculated weekly pay"""
    name = input("What is your first and last name? ")
    hours = int(input("How many hours did you work? "))
    rate = float(input("What is your hourly rate in dollars? "))
    if hours < 0:  # input validation for negative numbers
        return "No negative hours!"
    elif rate < 0:  # input validation for negative numbers
        return "No negative rates!"
    else:
        paycheck = weekly_pay(hours, rate)  # function call from function
        return "Name: " + name + ", Weekly Paycheck: $" + str(paycheck)


def weekly_pay(hours_1, rate_1):
    pay = hours_1*rate_1
    return pay


if __name__ == '__main__':
        try:
            print(hourly_employee_input())  # call function
        except ValueError:
            print("BAD INPUT!")

