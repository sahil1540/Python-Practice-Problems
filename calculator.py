print("===== SIMPLE CALCULATOR =====")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

a = get_number("Enter first number: ")
b = get_number("Enter second number: ")

print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if 1 <= choice <= 4:
            break
        print("Choose 1-4 only.")
    except ValueError:
        print("Enter a number 1-4.")

if choice == 1:
    print(f"Answer: {a + b}")
elif choice == 2:
    print(f"Answer: {a - b}")
elif choice == 3:
    print(f"Answer: {a * b}")
elif choice == 4:
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Answer: {a / b}")
