"""
Lena Aly

ask for string - function called when user input is required to be a string

"""


def ask_for_string(question, error_msg):
    valid = False

    while valid is False:
        response = input(question)
        if response != "":
            valid = True
        # if the input is blank then show error message and return as
        # false so calling function can act on it (will ask again)
        else:
            print(error_msg)
            valid = False
    return response


item_name = ask_for_string("Enter item name: ", "This cannot be blank - Please enter the Items name.")
