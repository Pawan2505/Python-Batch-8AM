# Lecture Notes: Python Built-in Functions

## Introduction
In Python, **built-in functions** are those that are available by default without importing any library. They help in performing common tasks like data manipulation, mathematical operations, and more.

## Categories of Built-in Functions

### 1. Mathematical Functions
- **`abs(x)`**: Returns the absolute value of `x`.
- **`pow(x, y)`**: Returns `x` raised to the power of `y`.
- **`min(a, b, c, ...)`**: Returns the smallest value.
- **`max(a, b, c, ...)`**: Returns the largest value.
- **`sum(iterable)`**: Returns the sum of values in the iterable.
- **`round(x, n)`**: Rounds the value of `x` to `n` decimal places.

```python
print(abs(-5))   # 5
print(pow(2, 3)) # 8
print(min(3, 7, 1))  # 1
print(max(3, 7, 1))  # 7
print(sum([1, 2, 3]))  # 6
print(round(3.1415, 2))  # 3.14
```

### 2. Sequence and Collection Functions
- **`len(obj)`**: Returns the length of an object.
- **`sorted(iterable)`**: Returns a sorted list from the iterable.
- **`all(iterable)`**: Returns `True` if all elements are true.
- **`any(iterable)`**: Returns `True` if any element is true.
- **`enumerate(iterable)`**: Adds index to an iterable.
- **`zip(iterable1, iterable2, ...)`**: Combines two or more iterables into a tuple.

```python
print(len("hello"))  # 5
print(sorted([3, 1, 2]))  # [1, 2, 3]
print(all([True, True]))  # True
print(any([False, True]))  # True
print(list(enumerate(['a', 'b'])))  # [(0, 'a'), (1, 'b')]
```

### 3. Input/Output Functions
- **`input()`**: Takes input from the user.
- **`print()`**: Prints to the console.
- **`open()`**: Opens a file to read or write.
- **`eval(expression)`**: Evaluates a Python expression.

```python
name = input("Enter your name: ")  # User input
print("Hello", name)
```

### 4. Type Conversion Functions
- **`int(x)`**: Converts to an integer.
- **`float(x)`**: Converts to a floating point.
- **`str(x)`**: Converts to a string.
- **`bool(x)`**: Converts to a boolean.

```python
print(int("10"))   # 10
print(float("3.5"))  # 3.5
print(str(100))  # "100"
print(bool(0))   # False
```

### 5. Object-Oriented Functions
- **`type(obj)`**: Returns the type of an object.
- **`isinstance(obj, class)`**: Checks if an object is an instance of a class.
- **`id(obj)`**: Returns the memory address of an object.

```python
x = [1, 2, 3]
print(type(x))  # <class 'list'>
print(isinstance(x, list))  # True
```

### 6. Miscellaneous Functions
- **`callable(obj)`**: Checks if an object can be called (i.e., if it's a function).
- **`hash(obj)`**: Returns the hash value of an object.
- **`getattr(obj, 'attr')`**: Returns the value of an object's attribute.

```python
def my_func(): pass
print(callable(my_func))  # True

my_dict = {"name": "Alice"}
print(getattr(my_dict, 'name'))  # Alice
```

---

## Note:
Built-in functions make Python programming easy by providing ready-made solutions for many common tasks. You don't need to write complex code for basic operations. These functions help you save time and write cleaner, more efficient code.

### Important Points:
- No need to import anything to use these functions.
- They help in tasks like calculations, handling sequences, type conversion, file I/O, and more.
