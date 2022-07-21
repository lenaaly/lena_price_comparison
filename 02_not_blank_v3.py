"""
Lena Aly

not blank - making sure the input is not blank

"""

name_list = []


def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_msg)


item_name = not_blank("Item name: ", "This cannot be blank - Please enter the Items name.")

