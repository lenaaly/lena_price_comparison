"""
Lena Aly

budget - asks the user for their budget and stores in a variable
budget v2 - calls the number checker function

"""


def user_budget(question):
    # will call number checker by using validBudget
    validBudget = False

    while validBudget is False:
        budget = input(question)
        validBudget = num_checker(budget, "Error - Please enter a budget above 0")
        if validBudget:
            return budget
