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
        except ValueError:
            print()
            print("Error: Please choose a valid option")
            continue
        if user_input == 6:
            break
menu()