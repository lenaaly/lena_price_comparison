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
base v5 - adding unit calculations and printing output of recommendations for user
base v6 - adding pandas for item information (aesthetics) and recommending best valued item to user

"""

# setting up functions****

# import dictionaries
import pandas as pd


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
        try:
            response = float(input(question))
            if response <= 0:
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
        response = input(question).lower()

        if response == "yes" or response == "y":
            valid = True
        elif response == "no" or response == "n":
            valid = True
            keepGoing = False
        else:
            print(error_msg)

    return keepGoing


# converting weight from g to kg function
def weight_kg(item_weight_kg):
    item_weight_kg = float(item_weight / 1000)
    return item_weight_kg


# calculating the unit price function
def unit_price(item_price, item_converted_weight):
    unit_calculation = float(item_price / item_converted_weight)
    return unit_calculation


# ************* MAIN ROUTINE ************

# set up lists
item_info = []
all_item_names = []
all_item_prices = []
all_item_weights = []
all_unit_prices = []

# set up dictionaries

items_table = {
    "Item name": all_item_names,
    "Price": all_item_prices,
    "Weight (kg)": all_item_weights,
    "Unit price (per kg)": all_unit_prices
}

# ask user for their budget once, calling ask for float function
budget = ask_for_float("Enter your budget: ", "This value is invalid - Enter a number over 0")
keepAskingForItems = True

# ask the user for the item name, price and weight
while keepAskingForItems:
    # asking for item name, calling ask for string function
    item_name = ask_for_string("Enter item name: ", "This value is invalid - Please enter the Items name.")
    all_item_names.append(item_name)

    # asking for items price, calling ask for float function
    item_price = ask_for_float("Enter item price: ",
                               "This value is invalid - In numbers over 0, enter the Items price.")
    all_item_prices.append(item_price)

    # asking for items weight, calling ask for float function
    item_weight = ask_for_float("Enter item weight in grams: ",
                                "This value is invalid - In numbers over 0, enter the Items weight in grams.")

    # item weight conversion from g to kg
    item_converted_weight = weight_kg(item_weight)
    all_item_weights.append(item_converted_weight)

    # call item unit price calculation
    calculated_unit_price = unit_price(item_price, item_converted_weight)
    all_unit_prices.append("{:.2f}".format(calculated_unit_price))

    # appending items into lists
    # item_info.append([all_item_names, item_price, item_converted_weight, "{:.2f}".format(calculated_unit_price)])
    # print()

    # ask if there are any more items
    ask_more_items = yes_no_items("Do you have any more items?: ", "This value is invalid - Enter yes / no")
    if ask_more_items is False:
        keepAskingForItems = False
    print()

# print information
items_frame = pd.DataFrame(items_table)
print(items_frame)
print(item_info)
