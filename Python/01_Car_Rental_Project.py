# Import libraries and set current directory
import os
import json
from pathlib import Path
os.chdir(Path(__file__).parent)


# Define variables
list_of_ids = [] 
wishes_list = [] 
receipt_text = ""
total_price = 0


# 1 Get Menu 
with open("01_Car_Rental_Inventory.json", mode ="r", encoding="UTF-8") as file:
    menu = json.load(file)


# 2 Greet
greeting = "\nWillkommen bei Autoverkauf Feser"
print(greeting)
print("~" * len(greeting))
print()
print("Das sind unsere Autos: ")


# 3 Show Menu
for category in menu:
    for inhalt in menu[category]:
        print(f'{inhalt["id"]}. {inhalt["brand"]} {inhalt["model"]}     \t{inhalt["price"]}€')
        list_of_ids.append(inhalt["id"])
    print()


# 4 User information
gastinfotext = "\nGastinfo"
print(gastinfotext)
print("~"*len(gastinfotext))
first_name =  input("Firstname: ").strip().title()
last_name =  input("Lastname: ").strip().upper()


# 5 User Wishes
userwishes = "\nIhre Wünsche: "
print(userwishes)
print("~"*len(userwishes))

while True:
    wish_id = int(input("Please enter the id of the cars you want to rent, when youre finished press 0: ")) 
    if wish_id == 0:
        print()
        break # exit point
    elif wish_id not in list_of_ids:
        print("This Car ID doesnt exist")
        continue
    wishes_list.append(wish_id)


# 6 Quittung
receipt_text = f"\nQuittung für Gast {first_name} {last_name}\n"
receipt_text += "~" * len(receipt_text) + "\n"

for number in wishes_list:
    for category in menu: 
        for inhalt in menu[category]:
            if number == inhalt["id"]:
                print(f'{inhalt["id"]}. {inhalt["brand"]} {inhalt["model"]}     \t{inhalt["price"]}€')
                total_price += inhalt["price"]

receipt_text += f"Summe: {total_price}€\n"
receipt_text += "Thank you for your visit"
print(receipt_text)


# 7 Quittung abspeichern als .txt datei
with open(f"receipt_for_{last_name}_{first_name}.txt", mode= "w", encoding= "UTF-8") as file:
        file.write(receipt_text)
