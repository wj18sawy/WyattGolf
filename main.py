import json
import os
import Bag

def open_bag(file_name):
    with open(file_name) as file:
        payload = json.loads(file.read())
        global my_bag
        my_bag = Bag.create_bag_from_payload(payload)

def save_bag(file_name):
    with open(file_name, "w") as write_file:
        json.dump(my_bag.__dict__, write_file)

options = ["A", "B", "C"]

print("Welcome to WyattGolf, open to new name suggestions...")
while True:
    print("Options (type letter of option and press enter) :")
    print("[A] Play Golf")
    print("[B] Range Session")
    print("[C] Edit Bag")
    choice = input("What would you like to do? : ")
    if(choice in options):
        break
    else:
        print(choice + " is not a valid option. Please select one of the following options")
        print(*options, sep = ", ")



# # Open bag and load to variable my_bag
# open_bag('WyattGolf/WyattsBag.json')


# # Save bag to file
# save_bag('WyattGolf/WyattsBag.json')

