# CSV Personal Finance Tracker

#### Video Demo: https://youtu.be/jxW-cfrKxTM

#### Description:

## How to Use

1. Make sure you have Python installed
2. Install pytest: `pip install -r requirements.txt`
3. Create an empty expenses.csv file or let the program create it by adding one expense
4. Run the program: `python project.py`
5. Run tests: `pytest test_project.py`

The main menu will guide you through all available options. Choose numbers to navigate menus and 'Q' or 'R' to quit or return to previous menus.

## Requirements

The program requires pytest for running tests. All other functionality uses Python's standard library (csv, sys, os, datetime), so no additional installations are needed for the main program.

This is a command-line expense tracker application built in Python that helps users manage and track their personal expenses. The program stores all expense data in a CSV file and provides various tools to view, search, and analyze spending patterns.

## Project Overview

The Expense Tracker is designed to be a simple yet comprehensive tool for personal finance management. I chose this project because I wanted to challenge myself, i struggled with week 6 File I/O of CS50P, and by creating something practical that could be used in daily life. Managing expenses manually in spreadsheets can be tedious, so I built this program to streamline the process with an easy-to-use menu system.

## Files Description

### project.py

This is the main file that contains all the core functionality of the expense tracker. The program is organized around a main menu system that branches into several sub-menus for different features.

The file includes the following key functions:

**main()** - This is the primary function that runs the entire program. It displays the main menu and handles user input to navigate to different features. The menu uses a while loop to keep the program running until the user chooses to quit. I structured it with multiple nested menus to keep related features grouped together logically.

**add_expense()** - Handles adding new expenses to the CSV file. It prompts the user for date, amount, category, and description. I included validation loops for each input to ensure data integrity. For example, the date must match DD-MM-YYYY format, and the amount must be a positive integer. If the user leaves the date blank, it automatically uses today's date. I decided to use integers for amounts to keep things simple and avoid floating-point precision issues.

**load_expenses()** - Reads and displays all expenses from the CSV file in a simple list format. This gives users a quick overview of all their spending.

**total_expenses()** - Calculates and displays the sum of all expenses in the CSV file. This function iterates through all rows, converts the amount strings to integers, and returns the total. I included this because knowing your total spending is fundamental to expense tracking.

**view_by_category()** - Groups and displays expenses organized by category. This was one of the more complex functions to implement. It creates a dictionary with categories as keys and lists of expenses as values, then displays them in a formatted table. I added formatting with string alignment to make the output easy to read.

**search_by_category()** - Allows users to search for all expenses in a specific category. This is useful when you want to see how much you've spent on one type of expense, like food or entertainment.

**view_by_date()** - Provides a submenu for searching expenses by day, month, or year. I broke this into three separate functions (search_by_day, search_by_month, search_by_year) to keep the code modular and easier to maintain.

**search_by_day()** - Searches for expenses on a specific date. Uses datetime validation to ensure the user enters a valid date.

**search_by_month()** - Searches for all expenses in a given month and year. I realized I didn't need datetime for this since I'm just comparing string segments, which made the code simpler.

**search_by_year()** - Similar to search_by_month but only requires a year input.

**add_category()** - Allows users to add custom categories beyond the default ones. The new category is appended to the CATEGORIES list and automatically capitalizes the input for consistency.

**delete_expense()** - Removes a specific expense from the CSV file. This was tricky to implement because CSV files don't support direct row deletion. My solution creates a temporary file, copies all rows except the one to delete, then replaces the original file with the temp file using os.replace(). The function requires exact matching of all fields (date, amount, category, description) to prevent accidental deletions.

**generate_excel_report()** - This is a placeholder function I plan to implement in the future using pandas or another library to export data to Excel format.

### expenses.csv

This is the data file where all expenses are stored. It uses CSV format with four columns: date, amount, category, and description. I chose CSV because it's simple, human-readable, and easy to work with using Python's csv module. The file must exist before running the program.

### requirements.txt

Lists all the external libraries needed to run this project. Currently it only includes pytest, which is needed to run the test functions. The rest of the program uses only Python's standard library.

### test_project.py

Contains pytest test functions for the expense tracker. I focused on testing functions that don't require user input:

test_total_expenses() - Creates a temporary CSV file with test data, calculates the total, and verifies it's correct. The test includes cleanup to remove the test file afterward.

test_add_category() - Tests that new categories are properly added to the CATEGORIES list and verifies the list length increases correctly.

test_add_category_duplicate() - Tests the behavior when adding a category that already exists. Currently the program allows duplicates, which I might change in future versions.

I also created a helper function called add_category_test() that mimics add_category() but without user input, making it testable.

## Design Choices

**Menu Structure**: I decided to use nested menus rather than a single flat menu because it organizes features logically and prevents the main menu from becoming overwhelming. Related features like "view all" and "search by category" are grouped under "View & Search Expenses."

**Date Format**: I chose DD-MM-YYYY format because it's more common internationally, the format is enforced with validation to maintain consistency in the CSV file.

**Category System**: I included a predefined list of common categories (Food, Transport, Bills, Entertainment, Shopping, Healthcare, Other) but allowed users to add custom ones. This balances convenience with flexibility. All category inputs are automatically capitalized for consistency.

**Delete Function**: I debated whether to require all fields (date, amount, category, description) for deletion or just some of them. I chose to require all fields to prevent accidental deletions of the wrong expense, even though it's more typing for the user. I also added a flag to ensure only the first matching expense is deleted if there are duplicates.

**File Organization**: I considered splitting functions into separate modules but kept everything in project.py to meet the course requirements and because the program isn't large enough to necessitate multiple files.

**Error Handling**: I used try-except blocks throughout to handle common errors like file not found or invalid input. Most errors print a message and either loop again or exit gracefully with sys.exit().

## Future Improvements

I plan to implement the Excel export feature using pandas or other libraries, add data visualization with charts, and possibly create a graphical interface. I'd also like to add budget tracking and alerts when spending exceeds set limits. Another feature would be monthly/yearly summaries and the ability to edit existing expenses without deleting and re-adding them.
I alsso belive that i could structure this programm in a oop way.
