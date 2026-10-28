store_a = {"Rice": 25, "Wheat": 40, "Sugar": 18}
store_b = {"Rice": 15, "Sugar": 12, "Oil": 20}

print("Store A Inventory:", store_a)
print("Store B Inventory:", store_b)

merged_inventory = {
    item: store_a.get(item, 0) + store_b.get(item, 0)
    for item in dict.fromkeys((*store_a, *store_b))
}

print("\nMerged Inventory:", merged_inventory)

item = input("\nEnter an item to check: ").title()
if item in merged_inventory:
    print(item, "total stock:", merged_inventory.get(item, 0))
else:
    print("Item not found in inventory.")

item = input("Enter an item to update: ").title()
quantity = int(input("Enter quantity to add: "))
merged_inventory[item] = merged_inventory.get(item, 0) + quantity

print("Updated Inventory:", merged_inventory)
