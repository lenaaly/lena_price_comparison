"""
Lena Aly

This is the base component - the program takes the users budget
and recommends which items are the best value for money, based on
the weight and price of the item. The program returns the best
recommended item within the users budget

base v1 - skeleton of program, setting up functions
base v2 - setting up functions: not blank component and item name component
base v3 - setting up functions: num checker, budget and item price

"""

# setting up functions*****

name_list = []


# item_info = [[name_list], [price_list], [weight_list]]

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


# no blank function, receives question and the error message and checks if question input is blank
def not_blank(question, error_msg):
    valid = False
    # if the question is blank then return as False
    if question == "":
        print(error_msg)
        valid = False
    # if the input is blank then show error message and return as false so calling function can act on it (will ask again)
    else:
        valid = True
    return valid


# item name function, takes valid items name and appends to a list
# Get the item name from the user and check if blank, and return the result
def item_name(question):
    name_response = input(question)

    while name_response != "xxx":
        name_response = input(question)
        if name_response == "xxx":
            return name_response

        elif name_response == "":
            not_blank(name_response, "This cant be blank - enter the items name")

        else:
            name_list.append(name_response)


# item price function, takes item price and appends to a list
def ask_price(question):
    # will call number checker by using validPrice
    validPrice = False

    while validPrice is False:
        item_price = input(question)
        validPrice = num_checker(item_price, "Error - Please enter a price above 0")
        if validPrice:
            return item_price

# item weight function, takes item weight and appends to a list

# weight g to kg calculation function, converts the weights from g to kg

# budget function, asks the user for the budget and stores in a variable
def user_budget(question):
    validBudget = False

    while validBudget is False:
        budget = input(question)
        validBudget = num_checker(budget, "Error - Please enter a number above 0")
        if validBudget:
            return budget


# *** MAIN ROUTINE ***

# asking the user what their budget is
user_budget("What is your budget?: ")

# asking the user the names of their items
item_name("Item name: ")
print(name_list)

# asking the user the price of their item
ask_price("Item price: ")

# asking the user the weight of their item
