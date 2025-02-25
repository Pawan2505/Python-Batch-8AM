# User-defined Functions in Python

# Function without parameters
def greet():
    # Prints a greeting message
    print("Hello, Welcome to Python!")

# Calling the greet function
greet()


# Function with parameters
def add(a, b):
    # Adds two numbers and prints the result
    result = a + b
    print(f"Sum: {result}")

# Calling the add function with arguments
add(5, 3)


# Function with return value
def multiply(a, b):
    # Returns the product of two numbers
    return a * b

# Storing the return value in result and printing it
result = multiply(4, 5)
print(result)


# Function with default arguments
def greet(name="User"):
    # Greets the user, defaulting to "User" if no argument is passed
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet("Alice")
greet()


# Function with variable-length arguments (*args)
def add_numbers(*args):
    # Adds an arbitrary number of numbers
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with multiple arguments
print(add_numbers(1, 2, 3, 4))


# Function with keyword arguments (**kwargs)
def show_info(**kwargs):
    # Prints information about a person using keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
show_info(name="John", age=30, city="Mumbai")


# Recursion example: Factorial function
def factorial(n):
    # Returns the factorial of a number using recursion
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the factorial function
print(factorial(5))  # Output: 120
