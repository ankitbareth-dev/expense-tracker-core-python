import uuid
import os
import csv
from functools import reduce
allowed_transaction_type = ["income","expense"]

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

def validate_choice(choice: int,allowed_choices : list[int]) -> bool:
    if choice in allowed_choices:
        return True
    else:  
        return False
def validate_transaction_input(): pass


def add_transaction():
    while True:
        transaction_type = input("Enter transaction type (income/expense): ").strip()
        if transaction_type not in allowed_transaction_type:
            print("Error :  Enter a valid transaction or check spelling")
            continue
        else:
            break
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
    date = input("Enter date (YYYY-MM-DD): ").strip()
    description = input("Enter description: ").strip()

    new_expense = {}
    new_expense["id"] = str(uuid.uuid4())
    new_expense["transaction_type"] = transaction_type
    new_expense["amount"] = amount
    new_expense["category"] = category
    new_expense["date"] = date
    new_expense["description"] = description

    transactions.append(new_expense)

    print("Expense added sucessfully")
    print()
    print(transactions[0])
    return

def view_all_transations():
    for expense in transactions:
        print(expense)
    return
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

    deleting_id = int(input("Enter transaction ID to delete: "))
    actual_id = transactions[deleting_id-1]["id"]
    transactions = [transaction for transaction in transactions if transaction["id"] != actual_id]
    print()
    print("Transaction Deleted Sucessfully")
    return


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


    

def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add transaction")
        print("2. View all transaction")
        print("3. View summary")
        print("4. Delete transaction")
        print("5. Export transaction to CSV")
        print("6. Exit")
        try:
            print()
            user_input : int = int(input("Choose an option: "))
            print()
            if validate_choice(user_input, list(range(1,7))):
                match user_input:
                    case 1:
                        add_transaction()
                        continue
                    case 2:
                        view_all_transations()
                        continue
                    case 3:
                        view_summary()
                        continue
                    case 4:
                        delete_transaction()
                        continue
                    case 5:
                        export_transactions_to_csv()
                        continue
            else:
                print("Error: Please choose between 1 to 6")
                continue
        except ValueError:
            print()
            print("Error: Please enter an integer")
            continue
        if user_input == 6:
            break
menu()