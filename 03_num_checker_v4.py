"""
Lena Aly

number checker - checks the input is an integer and no less than 0
number checker v2 - adding ValueError to raise for any unexpected input (not integer inputs)
number checker v3 - refining code to allow decimals to be entered
number checker v4 - reusable num checker

"""


def num_checker(question, error_msg):
    valid = False
    try:
        if float(question) <= 0:
            valid = False
            print(error_msg)
        else:
            valid = True
    except ValueError:
        valid = False
        print(error_msg)
    return valid
