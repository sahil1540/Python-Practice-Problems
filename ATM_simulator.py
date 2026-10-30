balance = 5000

def get_amount(prompt):
    while True:
        try:
            amt = float(input(prompt))
            if amt <= 0:
                print("Amount must be positive.")
                continue
            return amt
        except ValueError:
            print("Enter a valid number.")

while True:
    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Enter 1-4.")
        continue

    if choice == 1:
        print(f"Your balance is: Rs. {balance:.2f}")

    elif choice == 2:
        amount = get_amount("Enter deposit amount: ")
        balance += amount
        print(f"Deposited! New balance: Rs. {balance:.2f}")

    elif choice == 3:
        amount = get_amount("Enter withdrawal amount: ")
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn! New balance: Rs. {balance:.2f}")
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")
