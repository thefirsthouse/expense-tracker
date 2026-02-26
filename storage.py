"""Functions working with data"""

import os
import json
from typing import List

from expense import Expense

FILE_NAME = "data.json"


def load_expenses() -> List[Expense]:
    """Read expenses from disk and convert to Expense objects"""

    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, IOError):
        return []
    return [Expense.from_dict(item) for item in data]


def save_expenses(expenses: List[Expense]) -> None:
    """Serialize expense list and write it to the JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump([expense.to_dict() for expense in expenses], file, indent=4, default=str)
