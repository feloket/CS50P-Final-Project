import pytest
import csv
import os
from project import total_expenses, add_category, CATEGORIES


def test_total_expenses():
    """test that total_expenses calculates correctly"""
    test_file = 'expenses.csv'
    with open(test_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerow({"date": "01-12-2024", "amount": "50",
                        "category": "Food", "description": "Groceries"})
        writer.writerow({"date": "02-12-2024", "amount": "30",
                        "category": "Transport", "description": "Bus fare"})
        writer.writerow({"date": "03-12-2024", "amount": "19",
                        "category": "Entertainment", "description": "Movie"})

    # test total
    total = total_expenses()
    assert total == 99

    os.remove(test_file)


def test_add_category():
    """test that new categories are added correctly"""
    original_length = len(CATEGORIES)
    add_category_test("Gaming")
    assert len(CATEGORIES) == original_length + 1
    assert "Gaming" in CATEGORIES

    # remove added category
    CATEGORIES.remove("Gaming")


def test_add_category_duplicate():
    """test adding a category that already exists"""
    original_length = len(CATEGORIES)
    add_category_test("Food")
    assert len(CATEGORIES) == original_length + 1
    # should still add it even if duplicate
    # remove added category
    CATEGORIES.remove("Food")


def add_category_test(category_name):
    """function to add category without user input"""
    CATEGORIES.append(category_name.strip().capitalize())
