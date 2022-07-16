'''
not blank - making sure the input is not blank
'''
name_list = []

# receives question and the error message and checks if question input is blank
def not_blank(question, error_msg):
    valid = False
    if question != "":
        print(question)
    else:
        print(error_msg)


not_blank("Item name: ", "This cannot be blank - Please enter the Items name.")
