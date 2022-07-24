"""
Lena Aly

best items - recommend the best item based on the budget and prints it out

"""
import pandas as pd

test_items = [["salt crackers", 2.00, 0.185, 10.81], ["griffins snax", 2.50, 0.25, 10],
              ["pizza shapes", 3.30, 0.19, 17.37]]
headers = ["Item name", "Price", "Weight (kg)", "Unit price (per kg)"]

def best_item_selector(items_list, budget):
    best_item_frame = pd.DataFrame(test_items)
    # adding column headers to the panda
    best_item_frame.columns = headers

    # filter all objects above my budget
    best_items_frame_filtered = best_item_frame.query("`Price` <= @budget")
    best_items_frame_sorted = best_item_frame.sort_values(by=['Unit price (per kg)'])
    best_items_frame_filtered_sorted = best_items_frame_filtered.sort_values(by=['Unit price (per kg)'])

    best_item = best_items_frame_filtered_sorted.iloc[0][0]

    return best_item, best_items_frame_sorted

result = best_item_selector(test_items, 3)
print("------Sorted--------")
print(result[0])
print("------Filtered-------")
print(result[1])
print("------sorted and filtered-------")
print(result[2])
