"""
Lena Aly

weight to kg - converts the weight input from g to kg

"""


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


def weight_kg(item_weight_kg):
    item_weight_kg = float(item_weight / 1000)
    return item_weight_kg



item_weight = ask_for_float("Enter item weight in grams: ",
                            "This value is invalid - In numbers over 0, enter the Items weight in grams.")

item_converted_weight = weight_kg(item_weight)
print(item_converted_weight)
