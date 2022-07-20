"""
Lena Aly

ask for float - function called when user is asked to input float (number)

"""


def ask_for_float(question, error_msg):
    valid = False

    while valid is False:
        response = input(question)
        try:
            if float(response) <= 0:
                valid = False
                print(error_msg)
            else:
                valid = True
        except ValueError:
            valid = False
            print(error_msg)
    return response


item_weight = ask_for_float("Enter item weight: ", "Error")
