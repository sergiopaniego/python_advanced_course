# calculator.py
import sys

def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation")
            return
        
        print(f"The result is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    calculate()
