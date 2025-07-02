import csv
from inventory import read_inventory, add_item, update_quantity, write_inventory

def test_read_inventory(tmp_path):
    csv_file = tmp_path / 'inventory.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['item', 'quantity'])
        writer.writeheader()
        writer.writerow({'item': 'apple', 'quantity': 5})
        writer.writerow({'item': 'banana', 'quantity': 2})
    data = read_inventory(str(csv_file))
    assert data == {'apple': 5, 'banana': 2}

def test_add_item_new_and_existing():
    inv = {'apple': 5}
    add_item(inv, 'banana', 2)
    assert inv['banana'] == 2
    add_item(inv, 'apple', 3)
    assert inv['apple'] == 8

def test_update_quantity():
    inv = {'apple': 5}
    update_quantity(inv, 'apple', 10)
    assert inv['apple'] == 10


def test_write_inventory(tmp_path):
    inv = {'apple': 5, 'banana': 2}
    csv_file = tmp_path / 'out.csv'
    write_inventory(str(csv_file), inv)
    # Verify file contents
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == [
        {'item': 'apple', 'quantity': '5'},
        {'item': 'banana', 'quantity': '2'},
    ]
