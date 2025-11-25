import csv
import sys  # will use this to brake out of loops
from datetime import datetime

CATEGORIES = ['Food', 'Transport', 'Bills',
              'Entertainment', 'Shopping', 'Healthcare', 'Other']

EXPENSE_FILE = 'expenses.csv'

# recuerda ver los videos y archivos previos de file I/O de cs50


def main():
    # menu with options


def add_expense(date, amount, category, description):
    """adds new expenses"""
    ...


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
    total = 0
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['amount'])

    print(f"Total expenses: ${total:.2f}")
    return total


def view_by_category():
    """displays table with expenses by category"""
    ...


def generate_excel_report():
    """uses csv excel class to generate an excel report"""
    ...


def add_category():
    """adds new category to categories list"""
    ...


if __name__ == "__main__":
    main()
