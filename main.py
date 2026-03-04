from inventory import search_item, stock_alert
from vendor import generate_annual_purchase_report

while True:
    print("\n===== Automated Inventory & Vendor Billing System =====")
    print("1. Search Item by ID")
    print("2. Check Low Stock Alert")
    print("3. Generate Annual Purchase Report")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_id = int(input("Enter Item ID: "))
        item = search_item(item_id)

        if item:
            print("\nItem Found:")
            print("ID:", item[0])
            print("Name:", item[1])
            print("Stock:", item[2])
            print("Price:", item[3])
        else:
            print("Item not found.")

    elif choice == 2:
        low_stock = stock_alert()

        if low_stock:
            print("\n⚠ Low Stock Items:")
            for item in low_stock:
                print(item)
        else:
            print("All items have sufficient stock.")

    elif choice == 3:
        generate_annual_purchase_report()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")