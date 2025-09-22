def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            return f"The result is {num1 + num2}"
        case "-":
            return f"The result is {num1 - num2}"
        case "*":
            return f"The result is {num1 * num2}"
        case "/":
            if num2 != 0:
                return f"The result is {num1 / num2}"
            else:
                print("Cannot divide by zero.")
        case _:
            return "Please enter correct operator"

print(calculator())  


  
