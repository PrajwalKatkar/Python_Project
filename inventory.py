import numpy as np

inventory = [
    (101, "Pen", 50, 10),
    (102, "Notebook", 20, 50),
    (103, "Pencil", 5, 5),
    (104, "Eraser", 30, 3)
]

THRESHOLD = 10


def search_item(item_id):
    for item in inventory:
        if item[0] == item_id:
            return item
    return None


def stock_alert():
    low_stock_items = []
    for item in inventory:
        if item[2] < THRESHOLD:
            low_stock_items.append(item)
    return low_stock_items


def calculate_total_stock_value():
    stocks = np.array([item[2] for item in inventory])
    prices = np.array([item[3] for item in inventory])
    total_value = np.sum(stocks * prices)
    return total_value