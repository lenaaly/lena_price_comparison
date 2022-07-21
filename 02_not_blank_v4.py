"""
Lena Aly

not blank - making sure the input is not empty
not blank v4 - changing not blank function to be reusable

"""
name_list = []


# receives question and the error message and checks if question input is blank
def not_blank(question, error_msg):
    valid = False

    # if the question is not blank then return as true (its valid)
    if question != "":
        valid = True
    # if the input is blank then show error message and return as false so calling function can act on it (will ask again)
    else:
        print(error_msg)
        valid = False
    return valid


# not_blank("This cannot be blank - Please enter the Items name.")
