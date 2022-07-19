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

# number checker function, checks for valid numbers and invalid (letters / symbols / blank)
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

# ask user for string function (used in item name)

# ask user for float function (used in budget, item price and item weight)


# MAIN ROUTINE*****

# ask user for their budget once

# ask the user for the item name, price and weight
while keepAskingForItems:
    item_name = ask_for_string("Enter item name: ", "Error")
    item_price = ask_for_string("Enter item name: ", "Error")
    item_weight = ask_for_string("Enter item name: ", "Error")
    item_unit_price = item_weight/item_price
    iteminfo.append([item_name, item_price, item_weight, item_unit_price])
    moreitemstoadd = ask_for_string("More items to add yes or no: ", "Error")


    print(item_info)

# calculate unit price
# append to lists

# print lists
