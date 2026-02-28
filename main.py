import argparse
import sys

from service import (
    add_expense,
    delete_expense,
    list_expenses,
    summary,
    summary_by_month
)


def command_handler() -> dict:
    """Get cmd args and processes them into dict of commands"""

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", type=str, required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--month", type=int)

    # summary
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", required=False)

    args = parser.parse_args()

    return vars(args)


def main():
    if len(sys.argv) == 1:
        raw = input("Enter command: ")
        sys.argv += raw.split()
    command = command_handler()
    if not command:
        return
    
    cmd = command["command"]
    if cmd == "add":
        expense = add_expense(command["description"], command["amount"])
        print(f"Record {expense.id} added succesfully")
    elif cmd == "delete":
        delete_expense(command["id"])
    elif cmd == "list":
        list_expenses()
    elif cmd == "summary":
        if len(command) > 1:
            print(f"Summary for {command["month"]} - {summary_by_month(command['month'])}")
            pass
        print(f"Summary: {summary()}")


        


if __name__ == "__main__":
    main()
