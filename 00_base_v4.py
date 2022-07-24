"""
Lena Aly

This is the base component - the program takes the users budget
and recommends which items are the best value for money, based on
the weight and price of the item. The program returns the best
recommended item within the users budget

base v1 - skeleton of program, setting up functions
base v2 - setting up functions: not blank component and item name component
base v3 - setting up functions: num checker, budget and item price
base v4 - major changes to make code more flexible as explained on slide 33 of testing powerpoint

"""


# setting up functions****

# ask user for string function (used in item name)
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


# ask user for float function (used in budget, item price and item weight)
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


# asking user if they have any more items, yes / no function
def yes_no_items(question, error_msg):
    valid = False
    # keepGoing set to True so that when response is no, the program will stop asking item questions instead of looping
    keepGoing = True
    while not valid:
        response = input(question)

        if response == "yes" or response == "y":
            valid = True
        elif response == "no" or response == "n":
            valid = True
            keepGoing = False
        else:
            print(error_msg)

    return keepGoing


# MAIN ROUTINE*****

# set up lists
item_info = []

# ask user for their budget once
budget = ask_for_float("Enter your budget: ", "This value is invalid - Enter a number over 0")
keepAskingForItems = True

# ask the user for the item name, price and weight
while keepAskingForItems:
    item_name = ask_for_string("Enter item name: ", "This cannot be blank - Please enter the Items name.")
    item_price = ask_for_float("Enter item price: ",
                               "This value is invalid - In numbers over 0, enter the Items weight.")
    item_weight = ask_for_float("Enter item weight: ",
                                "This value is invalid - In numbers over 0, enter the Items weight.")
    item_unit_price = item_weight / item_price
    item_info.append([item_name, item_price, item_weight])
    print()
    ask_more_items = yes_no_items("Do you have any more items?: ", "This value is invalid - Enter yes / no")
    if ask_more_items is False:
        keepAskingForItems = False

    print()

print(item_info)

# calculate unit price
# append to lists

# print lists
