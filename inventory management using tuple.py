'''
Name: Adithya Manoj
Date: 19/11/2024
'''

inventory=[
    ("Laptop",5,30000.00),
    ("Headphones",15,500.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,3000.00)
]

highest_stock_value=0
item_with_highest_stock_value=None
for i in inventory:
    item,quantity,price= i
    stock_value=quantity*price
    print(f"Item Name:{item}, the Stock value is: {stock_value}")

    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item
print()
print(f"Item with the highest stock value: {highest_stock_value}")
print(f"Item with highest stock value is: {item_with_highest_stock_value}")