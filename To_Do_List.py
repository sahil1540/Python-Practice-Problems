print("MY TO DO LIST")

a = input("Enter task 1: ")
b = input("Enter task 2: ")
c = input("Enter task 3: ")
d = input("Enter task 4: ")
e = input("Enter task 5: ")
f = input("Enter task 6: ")

x = input("See today's list? ")

if x == "yes":

    print("YOUR TASKS:")
    print("1.", a)
    print("2.", b)
    print("3.", c)
    print("4.", d)
    print("5.", e)
    print("6.", f)

    y = input("Delete a task? ")

    if y == "yes":

        z = input("Enter task number: ")

        if z == "1":
            a = "[Deleted]"

        if z == "2":
            b = "[Deleted]"

        if z == "3":
            c = "[Deleted]"

        if z == "4":
            d = "[Deleted]"  
            
        if z == "5":
            e = "[Deleted]"
            
        if z == "6":
            f = "[Deleted]"    

        print("1.", a)
        print("2.", b)
        print("3.", c)
        print("4.", d)
        print("5.", e)
        print("6.", f)

else:
    print("Goodbye! Have A Nice Day ")
