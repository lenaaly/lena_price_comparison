"""
Lena Aly

item name v1 - takes the input from a user atleast once and prints
item name v2 - loops more than once and appends to name list

"""

name_list = []


def item_name(question):
    response = input(question)

    while response != "xxx":
        name_list.append(response)

        if response == "xxx":
            return response
        else:
            response = input(question)

item_name("Item name: ")
print(name_list)
