inventory = {"apple": 10, "banana": 5, "orange": 8}

def add_item(inventory, item, quantity):
    if item in inventory :
        inventory[item] += quantity
    else:
        inventory[item] =quantity
    return inventory
