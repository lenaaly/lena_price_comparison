"""
Lena Aly

budget - asks the user for their budget and stores in a variable

"""


def user_budget(question):
    budget = input(question)
    print("Your budget is ${}".format(budget))


user_budget("What is your budget?: ")
