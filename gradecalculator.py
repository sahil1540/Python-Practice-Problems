
print("=== Student Grade Calculator ===")

name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
programming = float(input("Enter Programming marks: "))

if not all(0 <= mark <= 100 for mark in [maths, physics, programming]):
    print("Error: Marks must be between 0 and 100.")
else:
    total = maths + physics + programming
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n=== Result ===")
    print("Student:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    if percentage >= 40:
        print("Status: PASS")
    else:
        print("Status: FAIL")
