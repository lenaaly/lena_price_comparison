"""
Lena Aly

item price - asks the user for the item price and appends to list
item price v2 - calls num checker and loops (similar code to user budget component)

"""

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


def ask_price(question):
    # will call number checker by using validPrice
    validPrice = False

    while validPrice is False:
        item_price = input(question)
        validPrice = num_checker(item_price, "Error - Please enter a price above 0")
        if validPrice:
            return item_price




ask_price("Item price: ")
