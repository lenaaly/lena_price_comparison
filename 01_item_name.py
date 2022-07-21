"""
Lena Aly

item name v1 - takes the input from a user atleast once and prints
"""


name_list=[]

def item_name(question):
    response = input(question)
    name_list.append(response)


item_name("Item name: ")
print(name_list)


