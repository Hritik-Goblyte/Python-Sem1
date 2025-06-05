import os
import random
import string
from datetime import datetime

MENU = {
    "Coffee": 2.50,
    "Tea": 1.75,
    "Sandwich": 5.00,
    "Cake": 3.50,
    "Juice": 2.00
}

RECORDS_FILE = 'cafe_records.txt'

def generate_bill_number():
    # Generate a random alphanumeric bill number
    bill_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return bill_number

def get_customer_details():
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    contact_number = input("Enter customer contact number: ")
    return name, address, contact_number

def display_menu():
    print("\n********* Cafe Menu *********")
    for item, price in MENU.items():
        print(f"{item:<15} ${price:.2f}")
    print("*****************************\n")

def update_menu():
    while True:
        print("\n1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Go Back")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            break
        else:
            print("Invalid option, please try again.")

def add_item():
    item = input("Enter the name of the new item: ")
    if item in MENU:
        print(f"{item} already exists in the menu.")
    else:
        price = float(input(f"Enter the price for {item}: "))
        MENU[item] = price
        print(f"{item} added to the menu with price ${price:.2f}")

def update_item():
    item = input("Enter the name of the item to update: ")
    if item in MENU:
        price = float(input(f"Enter the new price for {item}: "))
        MENU[item] = price
        print(f"Price of {item} updated to ${price:.2f}")
    else:
        print(f"{item} not found in the menu.")

def remove_item():
    item = input("Enter the name of the item to remove: ")
    if item in MENU:
        del MENU[item]
        print(f"{item} removed from the menu.")
    else:
        print(f"{item} not found in the menu.")

def print_bill(bill_number, name, address, contact_number, items, quantities, prices, date, tax_rate=0.07):
    print(f"\n********* Cafe Bill *********")
    print(f"Bill No.: {bill_number}")
    print(f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Customer Name: {name}")
    print(f"Customer Address: {address}")
    print(f"Customer Contact Number: {contact_number}")
    print(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
    print("="*45)
    
    subtotal = 0
    for item, qty, price in zip(items, quantities, prices):
        total = qty * price
        subtotal += total
        print(f"{item:<15}{qty:<10}{price:<10}{total:<10.2f}")
    
    tax = subtotal * tax_rate
    total_due = subtotal + tax
    
    print("="*45)
    print(f"{'Subtotal':<35}{subtotal:.2f}")
    print(f"{'Tax':<35}{tax:.2f}")
    print(f"{'Total Due':<35}{total_due:.2f}")
    print("="*45)
    print("Thank you for visiting!")
    print("****************************\n")
    
    return subtotal, tax, total_due

def save_record(bill_number, name, address, contact_number, items, quantities, prices, date, subtotal, tax, total_due):
    with open(RECORDS_FILE, 'a') as file:
        file.write(f"********* Cafe Bill *********\n")
        file.write(f"Bill No.:{bill_number}\n")
        file.write(f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Customer Address: {address}\n")
        file.write(f"Customer Contact Number: {contact_number}\n")
        file.write(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}\n")
        file.write("="*45 + "\n")
        
        for item, qty, price in zip(items, quantities, prices):
            total = qty * price
            file.write(f"{item:<15}{qty:<10}{price:<10}{total:<10.2f}\n")
        
        file.write("="*45 + "\n")
        file.write(f"{'Subtotal':<35}{subtotal:.2f}\n")
        file.write(f"{'Tax':<35}{tax:.2f}\n")
        file.write(f"{'Total Due':<35}{total_due:.2f}\n")
        file.write("="*45 + "\n")
        file.write("****************************\n\n")

def view_all_records():
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, 'r') as file:
            print(file.read())
    else:
        print("No records found.")

def view_today_sales():
    today = datetime.now().date()
    records_found = False
    
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, 'r') as file:
            for line in file:
                if line.startswith("Date: "):
                    date_str = line.split("Date: ")[1].strip()
                    record_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').date()
                    if record_date == today:
                        records_found = True
                        print("\n" + line.strip())  # Print the header line
                        for _ in range(6):
                            print(file.readline().strip())  # Print the next 6 lines of the record
                        print("="*45)
    if not records_found:
        print(f"No records found for {today.strftime('%Y-%m-%d')}.")

def view_specific_date():
    date_str = input("Enter the date (YYYY-MM-DD) to view records: ")
    try:
        specific_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    records_found = False
    
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, 'r') as file:
            for line in file:
                if line.startswith("Date: "):
                    record_date_str = line.split("Date: ")[1].strip()
                    record_date = datetime.strptime(record_date_str, '%Y-%m-%d %H:%M:%S').date()
                    if record_date == specific_date:
                        records_found = True
                        print("\n" + line.strip())  # Print the header line
                        for _ in range(6):
                            print(file.readline().strip())  # Print the next 6 lines of the record
                        print("="*45)
    if not records_found:
        print(f"No records found for {date_str}.")

def main():
    while True:
        print("\nWelcome to the Cafe Billing System")
        print("1. View Menu")
        print("2. Add New Record")
        print("3. View Old Records")
        print("4. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            display_menu()
            update_menu()
        elif choice == '2':
            bill_number = generate_bill_number()
            name, address, contact_number = get_customer_details()
            
            items = []
            quantities = []
            prices = []
            
            while True:
                item = input("Enter the item name (or type 'done' to finish): ")
                if item.lower() == 'done':
                    break
                if item not in MENU:
                    print("Item not in menu. Please choose from the menu.")
                    continue
                quantity = int(input(f"Enter the quantity for {item}: "))
                
                items.append(item)
                quantities.append(quantity)
                prices.append(MENU[item])
            
            date = datetime.now()
            subtotal, tax, total_due = print_bill(bill_number, name, address, contact_number, items, quantities, prices, date)
            save_record(bill_number, name, address, contact_number, items, quantities, prices, date, subtotal, tax, total_due)
        elif choice == '3':
            while True:
                print("\nView Old Records:")
                print("1. All Records")
                print("2. Today's Sales")
                print("3. Specific Date")
                print("4. Go Back")
                
                records_choice = input("Please select an option: ")
                
                if records_choice == '1':
                    view_all_records()
                elif records_choice == '2':
                    view_today_sales()
                elif records_choice == '3':
                    view_specific_date()
                elif records_choice == '4':
                    break
                else:
                    print("Invalid option, please try again.")
        elif choice == '4':
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
