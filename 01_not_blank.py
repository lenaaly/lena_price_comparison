'''

not blank v1 - takes the input from a user atleast once and prints

'''

name_list=[]

def not_blank(question):
    response = input(question)
    name_list.append(response)


not_blank("Item name: ")
print(name_list)

