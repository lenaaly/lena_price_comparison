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


# best item selector
def best_item_selector(items_list, budget):
    best_item_frame = pd.DataFrame(items_list)
    # adding column headers to the panda
    best_item_frame.columns = headers

    # filter all objects above my budget
    best_items_frame_filtered = best_item_frame.query("`Price` <= @budget")
    best_items_frame_sorted = best_item_frame.sort_values(by=['Unit price (per kg)'])
    best_items_frame_filtered_sorted = best_items_frame_filtered.sort_values(by=['Unit price (per kg)'])
    #check if the list is empty before getting the value, otherwise if list is empty we get an error
    if(best_items_frame_filtered_sorted.empty):
        best_item =0
    else:
        best_item = best_items_frame_filtered_sorted.iloc[0][0]

    return best_item, best_items_frame_sorted


# define test data to make it easier to test
test_items = [["salt crackers", 2.00, 0.185, 10.81], ["griffins snax", 2.50, 0.25, 10],
              ["pizza shapes", 3.30, 0.19, 17.37]]

# ************* MAIN ROUTINE ************

# set up list
item_info = []  # list to hold all items in it

# ask user for their budget once, calling ask for float function
budget = ask_for_float("Enter your budget: ", "This value is invalid - Enter a number over 0")
keepAskingForItems = True

# ask the user for the item name, price and weight
while keepAskingForItems:
    # asking for item name, calling ask for string function
    item_name = ask_for_string("Enter item name: ", "This value is invalid - Please enter the Items name.")
    # if item name is testdata then run test data and go out of while loop
    if (item_name == "testdata"):
        keepAskingForItems = False
        item_info = test_items
        break
    # asking for items price, calling ask for float function
    item_price = ask_for_float("Enter item price: ",
                               "This value is invalid - In numbers over 0, enter the Items price.")

    # asking for items weight, calling ask for float function
    item_weight = ask_for_float("Enter item weight in grams: ",
                                "This value is invalid - In numbers over 0, enter the Items weight in grams.")

    # item weight conversion from g to kg
    item_converted_weight = weight_kg(item_weight)

    # call item unit price calculation
    calculated_unit_price = unit_price(item_price, item_converted_weight)

    # appending item information to the list
    item_info.append([item_name, item_price, item_converted_weight, "{:.2f}".format(calculated_unit_price)])

    # ask if there are any more items
    ask_more_items = yes_no_items("Do you have any more items?: ", "This value is invalid - Enter yes / no")
    if ask_more_items is False:
        keepAskingForItems = False
    # adding a space/ new line
    print()

print("----------")
# adding list to the pandas
item_frame = pd.DataFrame(item_info)
# adding column headers to the panda
headers = ["Item name", "Price", "Weight (kg)", "Unit price (per kg)"]
item_frame.columns = headers
# print(item_frame)

best_recommendation = best_item_selector(item_frame, budget)
print(best_recommendation[1])
print("")
print("Your budget is ${:.2f}".format(budget))
best_recommendation_item = best_recommendation[0]
if(best_recommendation_item == 0):
    print("You dont have enough money in your budget")
else:
    print("The item recommended based on your budget is", best_recommendation[0])
