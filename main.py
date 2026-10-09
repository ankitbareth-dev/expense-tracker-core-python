from validator import validate_choice
import transactions

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print()
        print("1. Add transaction")
        print("2. View all transaction")
        print("3. View summary")
        print("4. Delete transaction")
        print("5. Export transaction to CSV")
        print("6. Exit")
        try:
            print()
            user_input : int = int(input("Choose an option: ").strip())
            print()
            if validate_choice(user_input, list(range(1,7))):
                match user_input:
                    case 1:
                        transactions.add_transaction()
                        continue
                    case 2:
                        transactions.view_all_transations()
                        continue
                    case 3:
                        transactions.view_summary()
                        continue
                    case 4:
                        transactions.delete_transaction()
                        continue
                    case 5:
                        transactions.export_transactions_to_csv()
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
main()