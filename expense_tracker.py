import csv
import os
from datetime import datetime

data_file = "expenses.csv"


def initialize_file():
    if not os.path.exists(data_file):
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense(category, description, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

def view_expenses():
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses recorded yet.")

def summary_by_category():
    category_totals = {}
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                category, amount = row[1], float(row[3])
                category_totals[category] = category_totals.get(category, 0) + amount
        for category, total in category_totals.items():
            print(f"{category}: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter category (Food, Transport, etc.): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            try:
                add_expense(category, description, float(amount))
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
