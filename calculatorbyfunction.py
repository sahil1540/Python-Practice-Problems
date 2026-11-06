
# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    return a / b


print("============================")
print("       MY CALCULATOR")
print("========************========")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))

elif choice == 2:
    print("Result:", subtract(num1, num2))

elif choice == 3:
    print("Result:", multiply(num1, num2))

elif choice == 4:
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", divide(num1, num2))

else:
    print("Invalid choice!")
