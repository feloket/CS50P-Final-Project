import csv
import sys  # will use this to brake out of loops
from datetime import datetime

CATEGORIES = ['Food', 'Transport', 'Bills',
              'Entertainment', 'Shopping', 'Healthcare', 'Other']

EXPENSE_FILE = 'expenses.csv'

# recuerda ver los videos y archivos previos de file I/O de cs50


def main():
    ...
    # menu with options

    # def add_expense(date, amount, category, description):
    #     """adds new expenses"""
    #     ...


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

# load_expenses() testing function


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
        with open(EXPENSE_FILE, 'r') as file:
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


# view_by_category() testing function


def view_by_date():
    """display expenses by date"""
    ...


def generate_excel_report():
    """uses csv excel class to generate an excel report"""
    ...


def add_category():
    """adds new category to categories list"""
    ...


if __name__ == "__main__":

    main()
