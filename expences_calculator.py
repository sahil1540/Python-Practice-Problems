print("===== EXPENSE TRACKER =====")

name = input("Enter your name: ")

balance = 5000
total_spent = 0

while True:

    print("\n1. Add Expense")
    print("2. Check Balance")
    print("3. Total Spent")
    print("4. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            total_spent += amount

            print("Expense added successfully!")
            print("Remaining balance:", balance)

        else:
            print("Invalid amount or insufficient balance!")

    elif choice == 2:

        print("Your balance is:", balance)

    elif choice == 3:

        print("Total money spent:", total_spent)

    elif choice == 4:

        print("Thank you for using Expense Tracker!")
        print("Goodbye,", name)
        break

    else:
        print("Invalid choice! Try again.")
