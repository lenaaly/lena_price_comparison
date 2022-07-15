'''

This is the base component - the program takes the users budget
and recommends which items are the best value for money, based on
the weight and price of the item. The program returns the best
recommended item within the users budget

base v1 - skeleton of program, setting up functions
base v2 - setting up functions: not blank component and item name component

'''

# setting up functions*****

# item_info=[[name_list], [price_list], [weight_list]]


# item name function, takes items name and appends to a list

name_list = []

def item_name(question):
    response = input(question)

    while response != "xxx":
        name_list.append(response)

        if response == "xxx":
            return response
        else:
            response = input(question)

# not blank function, makes sure input is not blank
def not_blank(question, error_msg):

    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_msg)


# item price function, takes item price and appends to a list

# item weight function, takes item weight and appends to a list

# weight g to kg calculation function, converts the weights from g to kg

# budget function, asks the user for the budget and stores in a variable

# *** MAIN ROUTINE ***

# asking the user the item name
not_blank("Item name: ", "This cannot be blank - Please enter the Items name.")
item_name("Item name: ")


#print(name_list)

# asking the user what their budget is

# asking the user the names of their items
