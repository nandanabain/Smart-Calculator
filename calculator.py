import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y        
def multiply(x, y):
    return x * y    
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def power(x, y):
    return x ** y
def factorial(n):
    if n < 0:
        raise ValueError("Cannot calculate the factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(x)
print("SMART CALCULATOR!")
while True:
    op = input("\n 1. Addition \n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Power\n 6. Square Root\n 7. Factorial\n 8. Exit\nEnter your choice: ")
    if op == "8":
        print("Thank you for using Smart Calculator!")
        break
    elif op in ['1', '2', '3', '4', '5', '6', '7']:
        if op == '6':
            x = float(input("Enter the number: "))
            try:
                print(f"The result is: {square_root(x)}")
            except ValueError as e:
                print(e)
        elif op == '7':
            x = int(input("Enter the number: "))
            try:
                print(f"The result is: {factorial(x)}")
            except ValueError as e:
                print(e)
        else:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if op == '1':
                print(f"The result is: {add(x, y)}")
            elif op == '2':
                print(f"The result is: {subtract(x, y)}")
            elif op == '3':
                print(f"The result is: {multiply(x, y)}")
            elif op == '4':
                try:
                    print(f"The result is: {divide(x, y):.2f}")
                except ValueError as e:
                    print(e)
            elif op == '5':
                print(f"The result is: {power(x, y)}")
    else:
        print("Invalid operation!")
