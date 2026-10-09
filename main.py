import uuid
allowed_transaction_type = ["income","expense"]

expenses = []

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

    expenses.append(new_expense)

    print("Expense added sucessfully")
    print()
    print(expenses[0])
    return

def view_all_transations():
    for expense in expenses:
        print(expense)
    return

def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add transaction")
        print("2. View all transaction")
        print("3. View summry")
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