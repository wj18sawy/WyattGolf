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


open_bag('WyattGolf/WyattsBag.json')
my_bag.name = "newName2"
save_bag('WyattGolf/WyattsBag.json')

