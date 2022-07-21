"""
Lena Aly

number checker - checks the input is an integer and no less than 0
number checker v2 - adding ValueError to raise for any unexpected input (not integer inputs)
number checker v3 - refining code to allow decimals to be entered

"""


def num_checker(question, error_msg):
    valid = False
    while not valid:
        try:
            number = float(input(question))

            if number <= 0:
                return number
                print(error_msg)
            else:
                break

        except ValueError:
            print(error_msg)

