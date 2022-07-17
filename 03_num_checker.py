"""
Lena Aly

number checker - checks the input is an integer and no less than 0

"""


def num_checker(question):
    number = int(input(question))

    if number >= "0":
        return number

    else:
        print("Error - enter an integer higher than 0")

num_checker("Number: ")
