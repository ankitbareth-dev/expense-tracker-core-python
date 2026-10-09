from validator import validate_choice
from transactions import add_transaction,view_all_transations,view_summary,delete_transaction,export_transactions_to_csv

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