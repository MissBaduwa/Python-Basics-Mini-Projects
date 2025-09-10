# ===============================
# Personal Expense Tracker - Covers Week 1 Python concepts
# ===============================

#Goal: Practice Python basics (variables, data structures, conditionals,
# loops, functions, modules, file handling, exception handling, and classes).


# --------- Imports ----------
import csv                          # To read/write CSV files
from tabulate import tabulate       # To display tables neatly
from datetime import datetime       # Handles dates


# --------- Expense Class ----------
# Blueprint for creating individual expense objects
class Expense:

    # Runs automatically when creating a new expense
    def __init__(self, amount, category, desc, date):
        self.amount = amount
        self.category = category
        self.desc = desc
        self.date = date

    # Converts the object into a dictionary
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "desc": self.desc,
            "date": self.date
        }


# --------- Functions ----------
# Add Expense Function
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g. Food, Transport): ").title()
        desc = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD, leave blank for today): ")

        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        # Validate date
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format! Using today’s date instead.")
            date = datetime.today().strftime("%Y-%m-%d")

        expense = Expense(amount, category, desc, date)
        expenses.append(expense)
        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Invalid amount! Please enter a number.")


# View Expenses Function
def view_expenses(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    table = [e.to_dict().values() for e in expenses]
    headers = ["Amount", "Category", "Description", "Date"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


# View Summary by Category
def view_summary(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount

    table = [(cat, amt) for cat, amt in summary.items()]
    print(tabulate(table, headers=["Category", "Total"], tablefmt="fancy_grid"))


# Save and Load Functions
def save_to_file(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "desc", "date"])
        writer.writeheader()
        for e in expenses:
            writer.writerow(e.to_dict())
    print(f"💾 Expenses saved to {filename}")


def load_from_file(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expense = Expense(float(row["amount"]), row["category"], row["desc"], row["date"])
                expenses.append(expense)
        print(f"📂 Loaded {len(expenses)} expenses from {filename}")
    except FileNotFoundError:
        print("⚠️ No saved file found. Starting fresh.")
    return expenses


# Sort Expenses Function
def sort_expenses(expenses):
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    sorted_expenses = sorted(expenses, key=lambda e: e.amount, reverse=True)
    table = [e.to_dict().values() for e in sorted_expenses]
    headers = ["Amount", "Category", "Description", "Date"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


# --------- Main Program ----------
def main():
    expenses = load_from_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Sort Expenses by Amount")
        print("5. Save Expenses")
        print("6. Exit")
        print("=============================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            sort_expenses(expenses)
        elif choice == "5":
            save_to_file(expenses)
        elif choice == "6":
            save_to_file(expenses)
            print("👋 Goodbye! Your expenses are saved.")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
