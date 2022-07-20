"""
Lena Aly

yes / no - after each item name is added, asks if the user has any more items and if yes continues, if no breaks

"""


def yes_no_items(question, error_msg):

    valid = False
    while not valid:
        response = input(question)
        if response == "yes" or response == "y":
            valid = True
        elif response == "no" or response == "n":
            valid = True
        else:
            valid == False
            print(error_msg)


    return response


ask_more_items = yes_no_items("Do you have any more items?: ", "This value is invalid - Enter yes / no")
