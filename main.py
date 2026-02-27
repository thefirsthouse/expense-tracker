import argparse
import sys

from service import (
    add_expense,
    delete_expense,
    list_expenses,
    summary
)


def command_handler() -> dict:
    """Get cmd args and processes them into dict of commands"""

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", type=str, required=True)
    add_parser.add_argument("--amount", type=float, required=True)

    # delete
    add_parser = subparsers.add_parser("delete")
    add_parser.add_argument("--id", type=int, required=True)

    # list
    add_parser = subparsers.add_parser("list")
    add_parser.add_argument("--month", type=int)

    # summary
    add_parser = subparsers.add_parser("summary")
    add_parser.add_argument("--month", required=False)

    args = parser.parse_args()

    return vars(args)


def main():
    print(summary())
    if len(sys.argv) < 1:
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
        # if len(command) > 2:
        #     print("Feature is not available on this version")
        #     return
        return summary()


        


if __name__ == "__main__":
    main()