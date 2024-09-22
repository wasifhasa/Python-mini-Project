# menu= {
# "pasta": 50,
# "pizza":20,
# "burger": 30,
# "water":25
# }
# print(menu)

# print("welcome to python restaurant")
# print("pizza:20\n pasta:50\n burger:30\n water:25")

# order_total = 0

# item_1 = input("Enter the item name = ")
# if item_1 in menu:
#     order_total += menu[item_1]
#     print(f"your item {item_1} has been added to your order")

# else:
#     print(f"Ordered item {item_1} is not available ")

# another_order = input(f"Do you want to add another item? (yes/no)")
# if another_order == "yes":
#         item_2 = input("Enter the name of second item =")
#         if item_2 in menu:
#             order_total += menu[item_2]
#             print(f"item {item_2} has been added to order")

#         else:
#             print(f"Ordered item {item_2} is not available in menu!")

# print(f"The total amount of items  to pay is {order_total}")            


menu = {
    "Pizza": 450,
    "Pasta": 500,
    "Coffee": 350,
    "Tea": 100,
    "Cold Drink": 70,
    "Water": 50
}

# Greet
print("Welcome to My Python Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available yet!")
    
    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_item != "yes":
        break

print(f"The total amount to pay is {order_total}.")