'''

not blank - making sure the input is not blank

'''

def not_blank(question):
    response = input(question)

    while response != "":
        if response == "":
            return response
        else:
            response = input(question)

not_blank("item name: ")
