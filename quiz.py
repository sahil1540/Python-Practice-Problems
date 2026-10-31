
score = 0

print("\n1. Which language is used for AI?")
print("1. HTML")
print("2. Python")
print("3. CSS")
answer = int(input("Enter your answer (1-3): "))

if answer == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Python.")

print("\n2. Which data type stores whole numbers?")
print("1. int")
print("2. float")
print("3. string")
answer = int(input("Enter your answer (1-3): "))

if answer == 1:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is int.")

print("\n3. Which keyword defines a function in Python?")
print("1. function")
print("2. def")
print("3. define")
answer = int(input("Enter your answer (1-3): "))

if answer == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is def.")

print("\n4. Which symbol is used for comments?")
print("1. //")
print("2. <!-- -->")
print("3. #")
answer = int(input("Enter your answer (1-3): "))

if answer == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is #.")

print("\n5. Which function displays output?")
print("1. input()")
print("2. print()")
print("3. output()")
answer = int(input("Enter your answer (1-3): "))

if answer == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is print().")
print("          QUIZ RESULT")

print("Your score:", score, "/ 5")

if score == 5:
    print("Excellent! Perfect score!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")

print("Thank you for playing!")
