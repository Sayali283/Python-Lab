#Develop modular Python programs using user-defined functions, recursion, and built-in modules to solve computational problems.
#user-defined functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))

#Recursion
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative integers")
else:
    print("Factorial:", factorial(num))
    
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))

if terms < 0:
    print("Enter a non-negative number")
else:
    for i in range(terms):
        print(fibonacci(i), end=" ")

#built-in modules
import math

num = float(input("Enter a positive number: "))

if num < 0:
    print("Please enter a non-negative number")
else:
    print("Square root:", math.sqrt(num))
    print("Square:", math.pow(num, 2))
    print("Ceiling:", math.ceil(num))
    print("Floor:", math.floor(num))
    print("Factorial of integer part:",
          math.factorial(int(num)))

import math

def get_number():
    return int(input("Enter a non-negative integer: "))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def calculate_square_root(n):
    return math.sqrt(n)

def calculate_power(n, exponent):
    return math.pow(n, exponent)

def main():
    num = get_number()

    if num < 0:
        print("Please enter a non-negative integer.")
        return

    print("Factorial:", factorial(num))
    print("Square root:", calculate_square_root(num))
    print("Square:", calculate_power(num, 2))

if __name__ == "__main__":
    main()
