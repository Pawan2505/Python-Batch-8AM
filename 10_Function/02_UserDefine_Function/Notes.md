# Lecture Notes: User-Defined Functions in Python

## Introduction
In Python, **functions** are blocks of code that can be reused and executed whenever required. A **user-defined function** is a function that you create, defining it with a specific name and set of instructions, so you can call and use it throughout your program.

Creating user-defined functions in Python helps to organize and modularize your code. It allows for reusability and makes code more readable and maintainable.

---

## 1. Syntax of User-Defined Functions

A user-defined function is created using the `def` keyword followed by the function name and parentheses. The function body (indented) contains the statements that are executed when the function is called.

### Basic Syntax:
```python
def function_name(parameters):
    # Function body
    statement(s)
    return value  # Optional
```

- **`def`**: This keyword is used to define a function.
- **`function_name`**: This is the name of the function, which should be descriptive.
- **`parameters`**: These are optional inputs to the function (also called arguments).
- **`return`**: This is optional. The `return` statement sends a result back to where the function was called.

---

## 2. Example of a Simple Function

### Example 1: Function without parameters
```python
def greet():
    print("Hello, Welcome to Python!")

# Function call
greet()
```

**Output**:
```
Hello, Welcome to Python!
```

- The function `greet` prints a greeting message when called.
- This function doesn't take any input parameters.

---

### 3. Functions with Parameters

Functions can take **inputs** (parameters), allowing you to customize their behavior.

### Example 2: Function with parameters
```python
def add(a, b):
    result = a + b
    print(f"Sum: {result}")

# Function call with arguments
add(5, 3)
```

**Output**:
```
Sum: 8
```

- Here, `a` and `b` are **parameters**, and when calling the function, we provide **arguments** `5` and `3`.

---

### 4. Return Statement

The **`return`** statement allows a function to return a value back to the caller. Without it, the function will return `None` by default.

### Example 3: Function with return value
```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
```

**Output**:
```
20
```

- The function `multiply` returns the product of `a` and `b`, which is then printed.

---

## 5. Types of Functions Based on Parameters

### a) Functions with No Parameters and No Return Value

```python
def display_message():
    print("This is a message.")

display_message()
```

- This function does not take any input and does not return anything.

### b) Functions with Parameters and No Return Value

```python
def greet_user(name):
    print(f"Hello {name}!")

greet_user("John")
```

- The function takes a parameter (`name`) and prints a greeting, but does not return anything.

### c) Functions with No Parameters but with Return Value

```python
def get_number():
    return 5

result = get_number()
print(result)
```

- The function returns a value (5), which is stored in `result` and then printed.

### d) Functions with Parameters and Return Value

```python
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

result = divide(10, 2)
print(result)
```

- The function `divide` takes two parameters and returns the result of division.

---

## 6. Default Arguments

In Python, you can provide default values for function parameters. If no value is passed when the function is called, the default value is used.

### Example: Function with default arguments
```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet("Alice")
greet()  # Default value "User" will be used
```

**Output**:
```
Hello, Alice!
Hello, User!
```

- Here, `name` has a default value of `"User"`, and when no argument is passed, it takes that default value.

---

## 7. Keyword Arguments

You can call a function by explicitly specifying the argument names. This is helpful when you have many parameters, and you want to pass only specific ones.

### Example: Keyword Arguments
```python
def person_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Call function using keyword arguments
person_info(age=25, city="Delhi", name="Ravi")
```

**Output**:
```
Name: Ravi, Age: 25, City: Delhi
```

- Here, the order of arguments is not important because we used **keyword arguments**.

---

## 8. Variable-length Arguments

Python allows you to pass a variable number of arguments to a function.

### a) *args (Non-keyword arguments)

- **`*args`** allows a function to accept any number of non-keyword arguments.

```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4))  # Output: 10
```

- The function can now accept any number of arguments, and we use a loop to add them.

### b) **kwargs (Keyword arguments)

- **`**kwargs`** allows a function to accept a variable number of keyword arguments.

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="John", age=30, city="Mumbai")
```

**Output**:
```
name: John
age: 30
city: Mumbai
```

- This allows you to pass keyword arguments in the form of a dictionary.

---

## 9. Recursion

A **recursive function** is a function that calls itself in order to solve smaller instances of the same problem.

### Example: Factorial using recursion
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

- The function calls itself repeatedly, reducing `n` by 1 each time until it reaches the base case (`n == 0`).

---

## Note:

User-defined functions in Python allow you to:

- Organize code into reusable blocks.
- Avoid code repetition and increase code clarity.
- Accept inputs and return results to make your code more flexible.

### Key Points:
- Use **`def`** to define a function.
- Functions can accept **parameters** and **return values**.
- You can use **default arguments**, **keyword arguments**, and **variable-length arguments**.
- Python allows **recursion**, where a function calls itself.
