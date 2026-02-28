"""CRUD"""

import datetime
from typing import Optional, List

from expense import Expense
from storage import load_expenses, save_expenses


def find_item(items: List, item_id: int) -> Optional[Expense]:
    """Returns item with given id or None"""
    for item in items:
        if item.id == item_id:
            return item
    return None


def add_expense(description: str, amount: float) -> Expense:
    """Forms an Expence objects and push it to the expenses list"""

    expenses = load_expenses()
    new_id = max((item.id for item in expenses), default=0) + 1
    today = datetime.date.today()
    expense = Expense(id=new_id, description=description, amount=amount, date=today)
    expenses.append(expense)
    save_expenses(expenses)
    return expense

def delete_expense(id: int) -> bool:
    """Deletes an expense from list"""

    expenses = load_expenses()
    expense = find_item(expenses, id)
    if expense:
        expenses.remove(expense)
        save_expenses(expenses)
        print(f"Record {expense.id} deleted successfully")
        return True
    print(f"Record {id} not found")
    return False


def update_expense(id: int, new_description: str) -> bool:
    """Updates an expense from list"""

    expenses = load_expenses()
    expense = find_item(expenses, id)
    if expense:
        expense.description = new_description
        save_expenses(expenses)
        return True
    return False

def list_expenses() -> None:
    expenses = load_expenses()
    for expense in expenses:
        print(expense.id, expense.description, expense.amount, expense.date)
    print("=== END ===")


def summary() -> float:
    expenses = load_expenses()
    return sum(expense.amount for expense in expenses)


def summary_by_month(month: int) -> float:
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            expense_month = datetime.datetime.strptime(expense.date, '%Y-%m-%d').month
            if expense_month == int(month):
                total += expense.amount
        except ValueError:
            continue # skip incorrect dates
    return total