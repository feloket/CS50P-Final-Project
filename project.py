import csv
import sys  # will use this to brake out of loops
from datetime import datetime

CATEGORIES = ['Food', 'Transport', 'Bills',
              'Entertainment', 'Shopping', 'Healthcare', 'Other']

EXPENSE_FILE = 'expenses.csv'  # dont like using this variable yet, may delete

# recuerda ver los videos y archivos previos de file I/O de cs50


def main():
    while True:
        print("\n---- Expense Tracker Menu ----")
        print("1: Add New Expense")
        print("2: View All Expenses")
        print("3: View Total Expenses")
        print("4: View Expenses by Category")
        print("5: Search by Category")
        print("Q: Quit")
        print("----------------------------")
        choice = input("What would you like to do? ").strip().upper()
        if choice == "Q":
            print("Exiting programm. Goodbye!")
            sys.exit()
        elif choice == "1":
            add_expense()
        elif choice == "2":
            load_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            search_by_category()

        # add menu options here, as they come.
        else:
            print("Invalid option, try again.")


def add_expense():
    """adds new expenses on user input"""
    # get date and validate format. may need to change to US format.
    while True:
        date = input("Enter date (DD-MM-YYYY)").strip()
        if not date:
            date = datetime.now().strftime('%d-%m-%y')
            break
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    # get amount
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("Must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. please enter a valid value")

    # get categrory
    for i, _ in enumerate(CATEGORIES, 1):
        print(f"Categories are: [{i}] {_} ")
    while True:
        choice = input("Enter category number: ").strip()
        try:
            index = int(choice) - 1
            if 0 <= index < len(CATEGORIES):
                category = CATEGORIES[index]
                break
            else:
                print("Invalid category number.")
        except ValueError:
            print("Please enter a number.")

    # get description
    description = input("enter description: ").strip()

    try:
        with open("expenses.csv", "a", newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=["date", "amount", "category", "description"])
            writer.writerow({"date": date, "amount": amount,
                            "category": category, "description": description})
            print(f"Expense added: {date} {amount} {category} {description}")
    except FileNotFoundError:
        sys.exit("File does not exist")


def load_expenses():
    """reads from csv file"""
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(
                    f"Date: {row['date']}, Amount: {row['amount']}, Category: {row['category']}, Description: {row['description']}")
    except FileNotFoundError:
        sys.exit("File does not exist")


def total_expenses():
    """displays total expenses"""
    try:
        total = 0
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total += float(row['amount'])

        print(f"Total expenses: ${total:.2f}")
        return total
    except FileNotFoundError:
        sys.exit("File does not exist")


def view_by_category():
    """displays table with expenses by category"""

    expenses_by_category = {cat: [] for cat in CATEGORIES}
    try:
        with open("expenses.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row['category']
                if category in expenses_by_category:
                    expenses_by_category[category].append(row)

        for category in CATEGORIES:
            expenses = expenses_by_category[category]
            if expenses:
                print(f"\n{category.upper()}")  # Category as tittle
                for expense in expenses:
                    date = expense.get('date', 'N/A')
                    desc = expense.get('description', 'N/A')
                    amount = float(expense.get('amount', 0))
                    print(f"  {date:<12} {desc:<30} ${amount:>8.2f}")

    except FileNotFoundError:
        print("File does not exist")
    except (KeyError, ValueError) as e:
        print(f"Error reading CSV: {e}")


def search_by_category():
    """search by category"""
    print(f"These are the available categories: {CATEGORIES}. ")
    search_cat = input(
        "Wich category to you want to search? ").strip().capitalize()
    try:
        with open("expenses.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['category'].capitalize() == search_cat:
                    print(
                        f"Date: {row['date']}, Amount: {row['amount']}, Description: {row['description']}")

    except FileNotFoundError:
        sys.exit("File does not exist")


def view_by_date():
    """display expenses by date"""
    ...


def generate_excel_report():
    """uses csv excel class to generate an excel report"""
    ...


def add_category():
    """adds new category to categories list"""
    ...


def delete_expense():
    """deletes selected expense"""
    ...


if __name__ == "__main__":
    main()
