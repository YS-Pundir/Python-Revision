inventory = {"apple": 10, "banana": 5, "orange": 8}

def add_item(inventory, item, quantity):
    if item in inventory :
        inventory[item] += quantity
    else:
        inventory[item] =quantity
    return inventory

def remove_item(inventory, item, quantity):
    if item in inventory:
        if inventory[item]>=quantity:
            inventory[item]-=quantity
        else:
            inventory.pop(item)
    else:
        print(f"{item} not found in inventory.")
    return inventory
    
def display_inventory(inventory):
    for item,quantity in inventory.items():
        print(f"{item}:{quantity}")

def manage_inventory(inventory):
    print("after adding items :")
    inventory=add_item(inventory,"banana",10)
    inventory=add_item(inventory,"grape",15)
    print(inventory)
    print("after removing items :")
    inventory=remove_item(inventory,"apple",5)
    inventory=remove_item(inventory,"orange",10)
    print(inventory)
    print("current inventory :")
    display_inventory(inventory)
manage_inventory(inventory)