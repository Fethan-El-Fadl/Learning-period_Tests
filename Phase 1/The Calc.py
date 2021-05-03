import turtle
print(" add = addition")
print("sub = substraction")
print("multiply = Multiplication")
print("divide = Divide")
    
terminate_program = False
while not terminate_program:
    n1 = turtle.textinput("Number1" ,"please enter a numberor quit to exit: ")
    if n1 == "quit":
        input("see ya")
        break
    n1 = float(n1)
    n2 = turtle.textinput("Number2" , "please enter another number: ")
    if n1 == "quit":
        print("see ya")
        break
    n2 = float(n2)

    while True:
        opr = input("Please enter add/sub/multiply/divide or quit to exit: ")
        if opr == "quit":
            terminate_program = True
            break
        if opr not in ["add" , "sub" , "multiply" , "divide"]:
             print("Unknown operation! Please enter add/sub/multiply/divide  or quit to exit:.")
             continue
        if opr == "add":
             print(n1, "+" , n2 , "=" , n1 + n2)
             input("Here is your result.....")
             break
        if opr == "sub":
            print(n1, "-" , n2 , "=" , n1 - n2)
            input("Here is your result.....")
            break
        if opr == "multiply":
            print(n1, "*" , n2 , "=" , n1*n2)
            input("Here is your result.....")
            break
        if opr == "divide":
            print(n1, "/" , n2 , "=" , n1/n2)
            input("Here is your result.....")
            break
