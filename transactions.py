import uuid
from functools import reduce
import os
import csv
import validator
import datetime


allowed_transaction_type = ("income","expense")

transactions = [
    {
        "id": str(uuid.uuid4()),
        "transaction_type": "income",
        "amount": 25000.0,
        "category": "Salary",
        "date": "2026-10-01",
        "description": "Monthly salary"
    },
    {
        "id": str(uuid.uuid4()),
        "transaction_type": "expense",
        "amount": 500.0,
        "category": "Food",
        "date": "2026-10-03",
        "description": "Lunch with friends"
    },
    {
        "id": str(uuid.uuid4()),
        "transaction_type": "expense",
        "amount": 1500.0,
        "category": "Travel",
        "date": "2026-10-05",
        "description": "Monthly travel expenses"
    },
    {
        "id": str(uuid.uuid4()),
        "transaction_type": "expense",
        "amount": 2000.0,
        "category": "Rent",
        "date": "2026-10-07",
        "description": "Room rent"
    },
    {
        "id": str(uuid.uuid4()),
        "transaction_type": "expense",
        "amount": 2000.0,
        "category": "Rent",
        "date": "2026-10-07",
        "description": "Room rent"
    }
]



def add_transaction():
    while True:
        print("1. Income")
        print("2. Expense")
        print()
        try:
          
            transaction_type = int(input("Enter transaction type : ").strip())
           
            if not validator.validate_choice(transaction_type,list(range(1,3))):
                print()
                print("Error: Please enter 1 or 2 only")
                print()
                continue
            else:
                break
        except ValueError:
            print()
            print("Error : Enter a valid option")
            print()
    while True:
        try:  
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("Error: Amount must be greater than 0")
                continue
            else:
                break
        except ValueError:
            print("Error : Please enter a valid amount")
            continue
        
    category = input("Enter category: ").strip()
    while True:
        date = input("Enter date (DD/MM/YYYY): ").strip()

        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
            break
        except ValueError:
            print("Error: Enter a valid date in DD/MM/YYYY format.")
    description = input("Enter description: ").strip()

    new_expense = {}
    new_expense["id"] = str(uuid.uuid4())
    new_expense["transaction_type"] = allowed_transaction_type[transaction_type-1]
    new_expense["amount"] = amount
    new_expense["category"] = category
    new_expense["date"] = date
    new_expense["description"] = description

    transactions.append(new_expense)

    print("Expense added sucessfully")
    print()
    return

def view_all_transations():
    print("=" * 60)
    print("             ALL TRANSACTIONS")
    print("=" * 60)

    if not transactions:
        print("No transactions found.")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction #{index}")
        print(f"Type:        {transaction['transaction_type'].title()}")
        print(f"Amount:      ₹{transaction['amount']:,.2f}")
        print(f"Category:    {transaction['category']}")
        print(f"Date:        {transaction['date']}")
        print(f"Description: {transaction['description']}")
        print("-" * 60)


def get_total_income():
    result = reduce(lambda a,b: a+b, [expense["amount"] for expense in transactions if expense["transaction_type"] == "income"  ],0)
    return result


def get_total_expenses():
    result = reduce(lambda a,b: a+b,[expense["amount"] for expense in transactions if expense["transaction_type"] == "expense"],0)
    return result

def get_expense_by_category():
    result = {}
    for expense in transactions:
        if expense["category"] not in result:
           result[expense["category"]] = expense["amount"]
        else:
            result[expense["category"]] += expense["amount"]
    return result

def view_summary():
    total_income = get_total_income()
    total_expenses = get_total_expenses()
    expense_by_category = get_expense_by_category()
    print("====== Financial Summary ======")
    print()
    
    print("Total Income:       ", total_income)
    print("Total Expenses:     ", total_expenses)
    print("Current Balance:    ",total_income-total_expenses)
    print()
    print("Total Transactions: ",len(transactions))
    print()
    print("====== Expense by Category ======")
    print()
    for cat in expense_by_category:
        print(f"{cat}: ₹{expense_by_category[cat]:,.2f}")
    return

def delete_transaction():
    global transactions
    print("====== Select Transaction to Delete ======")

    for index, transaction in enumerate(transactions):
        print(
            f"ID: {index+1}\n"
            f"Category: {transaction['category']} | "
            f"Amount: ₹{transaction['amount']:,.2f} | "
            f"Date: {transaction['date']}\n"
            f"Description: {transaction['description']}"
        )
        print("-" * 50)

    while True:
        try:
            deleting_id = int(input("Enter transaction ID to delete: "))
            actual_id = transactions[deleting_id-1]["id"]
            transactions = [transaction for transaction in transactions if transaction["id"] != actual_id]
            print()
            print("Transaction Deleted Sucessfully")
            return
        except ValueError:
            print("Error: Please select a  valid given choises")
            continue
        except IndexError:
            print("Error: Please select a valid id")


def export_transactions_to_csv():
    file_exists = os.path.exists("transactions.csv")
    file_is_empty = file_exists and os.path.getsize("transactions.csv") == 0

    try:
        with open("transactions.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "transaction_type",
                    "amount",
                    "category",
                    "date",
                    "description"
                ]
            )

            if not file_exists or file_is_empty:
                writer.writeheader()

            writer.writerows(transactions)

        print("Transactions exported successfully.")

    except OSError as error:
        print(f"Error exporting transactions: {error}")