'''

not blank v1 - takes the input from a user atleast once and prints
not blank v2 - takes multiple input and stops at exit code xxx

'''

name_list=[]

def not_blank(question):
    response = input(question)


    if response == "xxx":
        return response
    else:
        name_list.append(response)
        response = input(question)


not_blank("Item name: ")
print(name_list)

