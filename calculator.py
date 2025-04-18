def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                printreturn("Error: Division by zero is not allowed.")
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else: 
            print("Invalidoperator! Please use one of +, -, *, /, or %.")
            return
        print(f"Result: {num1} {operator} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
if __name__ == "__main__":
    calculator()
