# Import libraries and set current directory
import os
import json
from pathlib import Path
os.chdir(Path(__file__).parent)


list_of_ids = [] # the ids of all dishes
wishes_list = [] # user wishes (ids)
receipt_text = "" # text of the receipt
total_price = 0


# 1 Get the Menu from the JSON file
with open("menu.json", mode = "r", encoding="UTF-8") as file:
    menu = json.load(file)


# 2 Greeting
greeting = "\nWillkommen beim Leckerschmecker Restaurant"
print(greeting)
print("~" * len(greeting))
print()


# 3 Show Menu
for category in menu:
    print(category)
    print("~"*7)

    for dish in menu[category]:
        print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€')
        list_of_ids.append(dish["id"])
    print()


# 4 Get the Guest information
print("\nGastinfo")
print("~"*10)
first_name =  input("firstname: ").strip().title()
last_name =  input("lastname: ").strip().upper()


# 5 Get the Guest wishes
print("\nIhre Wünsche: ")
print("~"*10)

while True:
    wish_id = int(input("Please enter the id of the dish, when youre finished press 0: ")) # 100, 101, 203

    if wish_id == 0:
        break # exit point

    elif wish_id not in list_of_ids:
        print("The dish doesnt exist")
        continue

    wishes_list.append(wish_id)


# 6 Receipt
receipt_text = f"\nQuittung für Gast {first_name} {last_name}\n"
receipt_text += "~" * 30 + "\n"

for number in wishes_list:
    for category in menu: 
        for dish in menu[category]:
            if number == dish["id"]:
                print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€')
                total_price += dish["price"]


receipt_text += f"Summe: {total_price}€\n"
receipt_text += "Thank you for your visit"
print(receipt_text)


# 7 Save Receipt as .txt file
with open("quittung.txt", mode="w", encoding= "UTF-8") as file:
    file.write(receipt_text)

