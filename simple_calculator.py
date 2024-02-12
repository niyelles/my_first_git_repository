print("This is a Simple Calculator Script")
num1 = float(input("First number: "))
mathematical_operator = input("What mathematical operation do you want to take? [Only +, -, * and /] is allowed. \n")
num2 = float(input("Second number: "))

match mathematical_operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "/":
        print(num1 / num2)
    case "*":
        print(num1 * num2)
    case _:
        print("Invalid mathematical operator Input")
