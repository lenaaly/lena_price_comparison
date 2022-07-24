"""
Lena Aly

unit price calculation - takes the item price and item weight and calculates the items unit price

"""


# ask for float
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


# converts item weight in g to kg
def weight_kg(item_weight_kg):
    item_weight_kg = float(item_weight / 1000)
    return item_weight_kg


# takes item price and item weight in kg and calculates unit price
def unit_price(item_price, item_converted_weight):
    unit_calculation = float(item_price / item_converted_weight)
    return unit_calculation


# ask the user for the item weight
item_weight = ask_for_float("Enter item weight in grams: ",
                            "This value is invalid - In numbers over 0, enter the Items weight in grams.")

# ask the user for the item price
item_price = ask_for_float("Enter item price: ",
                           "This value is invalid - In numbers over 0, enter the Items price.")

# call calculations
item_converted_weight = weight_kg(item_weight)
calculated_unit_price = unit_price(item_price, item_converted_weight)

# printing item unit price and item weight in kg
print()
print("Item weight: {} kg".format(item_converted_weight))
print("Unit price: ${:.2f}".format(calculated_unit_price))
