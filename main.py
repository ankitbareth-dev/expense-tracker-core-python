def validate_choice(choice,allowed_choices):
    if choice in allowed_choices:
        return True
    else: 
        return False

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
                print("works")
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