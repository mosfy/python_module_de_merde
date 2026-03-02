import sys

def parse_inventory(argv):
    inventory = dict()
    for arg in argv:
        try:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
        except ValueError:
            print("Invalid item format:", arg)
            print("Expected format: name:quantity")
    return inventory

def print_inventory_report(inventory):
    total_items = sum(inventory.values())
    unique_types = len(inventory)

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_types)

    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        if total_items > 0:
            percent = (qty / total_items) * 100
        else:
            percent = 0

        if qty > 1:
            unit_text = "units"
        else:
            unit_text = "unit"

        print(f"{item}: {qty} {unit_text} ({percent:.1f}%)")

    most_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)

    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_item} ( {inventory[most_item]} units)")
    print(f"Least abundant: {least_item} ( {inventory[least_item]} units)")

    moderate = dict()
    scarce = dict()
    for item, qty in inventory.items():
        if qty >= 3:
            moderate[item] = qty
        else:
            scarce[item] = qty

    print("=== Item Categories ===")
    print("Moderate:", moderate)
    print("Scarce:", scarce)

    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)

    if restock:
        print("=== Management Suggestions ===")
        print(f"Restock needed:", end="")
        first = True
        for stock in restock:
            if not first:
                print(", ", end="")
            print(stock, end="")
            first = False
        print()


    print("=== Dictionary Properties Demo ===")

    print("Dictionary keys:", end="")
    first = True
    for key in inventory.keys():
        if not first:
            print(", ", end="")
        print(key, end="")
        first = False
    print()  

    print("Dictionary values:", end="")
    first = True
    for value in inventory.values():
        if not first:
            print(", ", end="")
        print(value, end="")
        first = False

    sample_item = "sword"
    print("\nSample lookup - '{}' in inventory:".format(sample_item), sample_item in inventory)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        sys.exit(0)

    inventory = parse_inventory(sys.argv[1:])
    print_inventory_report(inventory)