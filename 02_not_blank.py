'''

not blank - making sure the input is not blank

'''

def not_blank(question):
    response = input(question)

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            return response
        else:
            response = input(question)

not_blank("item name: ")
