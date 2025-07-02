# inventory module
from typing import Dict
import csv

Inventory = Dict[str, int]

def read_inventory(path: str) -> Inventory:
    """Load inventory data from a CSV file with columns item,quantity"""
    inventory: Inventory = {}
    try:
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = row['item']
                qty = int(row['quantity'])
                inventory[item] = qty
    except FileNotFoundError:
        pass
    return inventory

def add_item(inventory: Inventory, item: str, quantity: int = 1) -> None:
    """Add an item or increase its quantity"""
    inventory[item] = inventory.get(item, 0) + quantity

def update_quantity(inventory: Inventory, item: str, quantity: int) -> None:
    """Set the quantity for a specific item"""
    inventory[item] = quantity

def write_inventory(path: str, inventory: Inventory) -> None:
    """Write inventory to a CSV file"""
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['item', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item, qty in inventory.items():
            writer.writerow({'item': item, 'quantity': qty})
