import csv
import sys  # will use this to brake out of loops
import os # file operations 
from datetime import datetime

CATEGORIES = ['Food', 'Transport', 'Bills',
              'Entertainment', 'Shopping', 'Healthcare', 'Other']

FIELDNAMES = ["date", "amount", "category", "description"]
EXPENSE_FILE = 'expenses.csv'  # dont like using this variable yet, may delete

# recuerda ver los videos y archivos previos de file I/O de cs50
# recuerda ver videos de la libreria os

def main():
    while True:
        print(3*"-"+"Expense Tracker Menu"+3*"-")
        print("1: Add New Expense")
        print("2: View & Search Expenses")
        print("3: Reports & Tools (Total/Excel)")
        print("4: Manage Categories")
        # add future options here "6: Delete Expense"
        print("Q: Quit Program")
        print(10*"=")
        # get user choice
        choice = input("What would you like to do? ").strip().upper()
        if choice == "Q":
            print("Exiting programm. Goodbye!")
            sys.exit()
        # add expense
        elif choice == "1":
            add_expense()
        elif choice == "2":
            while True:
                print(3*"-"+"View & search menu"+3*"-")
                print("1: View All Expenses (List)")
                print("2: View Expenses by Category (Grouped List)")
                print("3: Search by Specific Category")
                print("4: Search by Date")
                print("5: Delete Expense")  # may put the delete function here
                print("R: Return to Main Menu")
                print(10*"=")
                # get use input
                choice_2 = input("Enter view/search choice: ").strip().upper()
                if choice_2 == "R":
                    break  # Exit loop, returns to main menu
                # view expense list
                elif choice_2 == "1":
                    load_expenses()
                # view by category
                elif choice_2 == "2":
                    view_by_category()
                # view by specific category
                elif choice_2 == "3":
                    search_by_category()
                # view by date
                elif choice_2 == "4":
                    view_by_date()
                # deletes specific expense
                elif choice_2 == "5":
                    delete_expense()
                else:
                    print("Invalid option!, try again")
        elif choice == "3":
            while True:
                print(3*"-"+"Reports & Tools Menu" + 3*"-")
                print("1: View Total Expenses (Sum)")
                print("2: Generate Excel Report")
                print("R: Return to Main Menu")
                print(10*"-")

                choice_3 = input(
                    "Enter reports/tools choice: ").strip().upper()

                if choice_3 == "R":
                    break  # Exit loop, returns to main menu
                #  view sumed expenses
                elif choice_3 == "1":
                    total_expenses()
                # need to finish this function
                elif choice_3 == "2":
                    generate_excel_report()
                else:
                    print("Invalid option!, try again")

        elif choice == "4":
            while True:
                print(3*"-"+"Category Management Menu" + 3*"-")
                print("1: Add New Category")
                print("2: View Available Categories")
                print("R: Return to Main Menu")
                print(10*"-")

                choice_4 = input("Enter category choice: ").strip().upper()

                if choice_4 == "R":
                    break  # Exit loop, returns to main menu
                # adds new category
                elif choice_4 == "1":
                    add_category()
                # prints categories
                elif choice_4 == "2":
                    for category in CATEGORIES:
                        print(f"Category: {category}")
                else:
                    print("Invalid option!, try again")

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
        with open("expenses.csv", "a", newline='', encoding='utf-8') as file:
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
        with open("expenses.csv", "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(
                    f"Date: {row['date']}, Amount: {row['amount']}, Category: {row['category']}, Description: {row['description']}")
    except FileNotFoundError:
        sys.exit("File does not exist")


def total_expenses():
    """displays sumed total of expenses"""
    try:
        total = 0
        with open("expenses.csv", "r", newline='', encoding='utf-8') as file:
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
        with open("expenses.csv", 'r', newline='', encoding='utf-8') as file:
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
        with open("expenses.csv", 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['category'].capitalize() == search_cat:
                    print(
                        f"Date: {row['date']}, Amount: {row['amount']}, Description: {row['description']}")

    except FileNotFoundError:
        sys.exit("File does not exist")


def view_by_date():
    """display expenses by date"""
    # get and  validate date
    print("\nOptions: ")
    print("1: Search by day")
    print("2: Search by month")
    print("3: Search by year")
    print("R: return to previus menu ")
    while True:
        choice = input("Enter your choice: ").strip().upper()
        # returns to previus menu
        if choice == "R":
            return
        elif choice == "1":
            search_by_day()
        elif choice == "2":
            search_by_month()
        elif choice == "3":
            search_by_year()
        else:
            print("Invalid option!, try again.")


def search_by_day():
    """search expenses by specific day"""
    while True:
        try:
            # ask the user for date input
            day = input("Enter day (1-31): ").strip()
            month = input("Enter month (1-12): ").strip()
            year = input("Enter year (YYYY): ").strip()
            # validate and format date
            date = datetime(int(year), int(month), int(day))
            search_date = date.strftime('%d-%m-%Y')
            with open("expenses.csv", 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['date'] == search_date:
                        print(
                            f"Date: {row['date']}, Amount: {row['amount']}, Description: {row['description']}")
        except ValueError as e:
            print(f"Invalid date! {e}")
        except FileNotFoundError:
            sys.exit("File does not exist")
        except KeyError:
            print("date' column not found in CSV!")
            break


def search_by_month():  # dont need datetime for non dd-mm-yyyy formats!
    """search expenses by specific month"""
    while True:
        try:
            # ask the user for date input
            month = input("Enter month (1-12): ").strip()
            year = input("Enter year (YYYY): ").strip()

            # validate month and year
            if not (month.isdigit() and 1 <= int(month) <= 12):
                print("Invalid month! Must be 1–12.")
                continue

            if len(year) != 4 or not year.isdigit():
                print("Invalid year! Use YYYY.")
                continue

            # format month to MM format
            month = f"{int(month):02d}"

            with open("expenses.csv", 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    day, row_month, row_year = row['date'].split('-')
                    if row_month == month and row_year == year:
                        print(
                            f"Date: {row['date']}, Amount: {row['amount']}, Description: {row['description']}"
                        )
        except ValueError as e:
            print(f"Invalid date! {e}")
        except FileNotFoundError:
            sys.exit("File does not exist")
        except KeyError:
            print("date' column not found in CSV!")
        break


def search_by_year():  # dont need datetime for non dd-mm-yyyy formats!
    """search expenses by specific year"""
    while True:
        try:
            # ask the user for date input
            year = input("Enter year (YYYY): ").strip()

            # validate year
            if len(year) != 4 or not year.isdigit():
                print("Invalid year! Use YYYY.")
                continue

            with open("expenses.csv", 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    day, month, row_year = row['date'].split('-')
                    if row_year == year:
                        print(
                            f"Date: {row['date']}, Amount: {row['amount']}, Description: {row['description']}"
                        )
        except ValueError as e:
            print(f"Invalid date! {e}")
        except FileNotFoundError:
            sys.exit("File does not exist")
        except KeyError:
            print("date' column not found in CSV!")
        break


def generate_excel_report():
    """uses csv excel class to generate an excel report"""
    # i want to call this function when the users selectsa a menu option and ask if he wants to export to excel
    # might delete, must lear pandas or something else for this. :,c
    ...


def add_category():
    """adds new category to categories list"""
    new_category = input("Enter new category: ").strip().capitalize()
    CATEGORIES.append(new_category)


def delete_expense():
    """deletes selected expense""" 
    # get date 
    while True:
        date = input("Enter date to delete (DD-MM-YYYY): ").strip()
        if not date:
            date = datetime.now().strftime('%d-%m-%Y')
            break
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    # get amount
    while True:
        try:
            amount = float(input("Enter amount to be deleted: ").strip())
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
    
    # csv doesnt handle row deletion
    # must create a new file without the selected row!
    filename = 'expenses.csv'
    temp_file = filename + '.tmp'
    deleted = False
    
    try:
        # had to merge this together.
        with open(filename, 'r', newline='', encoding='utf-8') as oldfile, \
             open(temp_file, 'w', newline='', encoding='utf-8') as newfile:
            
            reader = csv.DictReader(oldfile)
            writer = csv.DictWriter(newfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            
            for row in reader:
                # debug print to see what we're comparing
                print(f"Checking: date={row['date']}, amount={row['amount']}, category={row['category']}, desc={row['description']}")
                
                # compare with normalized values
                if (row['date'] == date and 
                    float(row['amount']) == amount and 
                    row['category'] == category and 
                    row['description'] == description and 
                    not deleted):
                    deleted = True
                    print("Expense found and will be deleted!")
                    continue
                writer.writerow(row)
        
        if deleted:
            os.replace(temp_file, filename)
            print("Expense removed")
        else:
            os.remove(temp_file)
            print("Expense not found in file.")
            
    except FileNotFoundError:
        sys.exit("File does not exist")
        

if __name__ == "__main__":
    main()
