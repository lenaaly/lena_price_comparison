'''

This is the base component - the program takes the users budget
and recommends which items are the best value for money, based on
the weight and price of the item. The program returns the best
recommended item within the users budget

base v1 - skeleton of program, setting up functions
base v2 - setting up functions: not blank component and item name component

'''

# setting up functions*****


name_list = []


# item_info = [[name_list], [price_list], [weight_list]]

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


# item name function, takes items name and appends to a list
# Get the item name from the user and check if blank, and return the result
def item_name(question):
    response = input(question)

    while response != "xxx":
        name_list.append(response)
        if response == "xxx":
            return response
        else:
            not_blank(response, "This cant be blank - enter the items name")
            response = input(question)




# item price function, takes item price and appends to a list

# item weight function, takes item weight and appends to a list

# weight g to kg calculation function, converts the weights from g to kg

# budget function, asks the user for the budget and stores in a variable

# *** MAIN ROUTINE ***

# asking the user what their budget is

# asking the user the names of their items
item_name("Item name: ")
print(name_list)

