"""
Lena Aly

best items - recommend the best item based on the budget and prints it out

"""
import pandas as pd

test_items = [["salt crackers", 2.00, 0.185, 10.81], ["griffins snax", 2.50, 0.25, 10],
              ["pizza shapes", 3.30, 0.19, 17.37]]

item_frame = pd.DataFrame(test_items)
# adding column headers to the panda
item_frame.columns = ["Item name", "Price", "Weight (kg)", "Unit price (per kg)"]

# using sort by feature from pandas to sort by unit price
print(item_frame.sort_values(by=['Unit price (per kg)']))


