"""
Lena Aly

number checker - checks the input is an integer and no less than 0

"""


def num_checker(question):
    number = int(input(question))

    valid = False

    while not valid:
        number = int(input(question))
        if number <= "0":
            print("error")
        else:
            print("valid")


num_checker("Number: ")
