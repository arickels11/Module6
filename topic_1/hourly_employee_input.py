"""CIS 189
Alex Rickels
Topic 1 Assignment 1"""


def hourly_employee_input():
    """this function gets user input for name, hours, and hourly rate and prints the information"""
    name = input("What is your first and last name? ")
    hours = int(input("How many hours did you work? "))
    rate = float(input("What is your hourly rate in dollars? "))
    if hours < 0:  # input validation for negative numbers
        print("No negative hours!")
    elif rate < 0:  # input validation for negative numbers
        print("No negative rates!")
    else:
        print("employee: ", name, ", hours worked: ", hours, ", hourly rate: $", rate)



if __name__ == '__main__':
    try:  # exception handling
        hourly_employee_input()  # call function
    except ValueError:
        print("BAD INPUT")
