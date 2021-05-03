terminate = False
while not terminate:
    n1 = input("Please enter a number: ")
    n1 = int(n1)
    n2 = input("Please enter another number: ")
    n2 = int(n2)

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add" , "sub"]:
            print("Unknown operation! ")
            continue
        if operation == "add":
            print("Result is" , n1 + n2 )
            break
        if operation == "sub":
            print("Result is" , n1 - n2 )
            break
