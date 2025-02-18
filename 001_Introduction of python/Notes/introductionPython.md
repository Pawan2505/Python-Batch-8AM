# 📖 **Lecture Notes: Introduction to Python**  
---

## **📌 1. Introduction to Python**  
Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It is widely used in web development, data science, automation, AI, and more.

### **🚀 Key Features of Python:**
✅ Simple and easy to learn  
✅ Dynamically typed (no need to declare variable types)  
✅ Interpreted (runs code line by line)  
✅ Case-sensitive  
✅ Supports multiple programming paradigms (OOP, functional, procedural)  

---

## **📌 2. History of Python**
- Created by **Guido van Rossum** in **1991**.
- Designed to be **beginner-friendly** with an emphasis on code readability.
- Named after the British comedy group **Monty Python**.

---

## **📌 3. Python Syntax and Print Function**
The `print()` function is used to display output in Python.

### **📝 Syntax:**
```python
print(object(s), sep='separator', end='end_character')
```
- **object(s)** → The values to be printed.  
- **sep** → Defines a separator (default is space).  
- **end** → Defines what appears at the end (default is a newline `\n`).  

### **🖥️ Example Code:**
```python
print("Hello, Python developers!")  # Output: Hello, Python developers!
print("Hello", "Bhai")  # Output: Hello Bhai
print("Hey", "Bro", "How are you?", sep=" - ")  # Output: Hey - Bro - How are you?
print("Hello", end="***")  # Output: Hello***
print("World")
```

---

## **📌 4. Variables and Data Types**
### **🛠️ Variables in Python**
- Python is **dynamically typed**, meaning you don’t need to declare variable types explicitly.
- Variables store values that can be of different data types.

### **💡 Example:**
```python
A = 10  # Integer
print(A, type(A))  # Output: 10 <class 'int'>

A = 12.7  # Float
print(A, type(A))  # Output: 12.7 <class 'float'>
```

---

## **📌 5. Constants in Python**
Python doesn’t have built-in constant variables, but we can create a class to prevent reassignment.

### **🚨 Example:**
```python
class Constant:
    def __setattr__(self, name, value):
        if hasattr(self, name):  
            raise TypeError(f"Cannot modify constant '{name}'")
        super().__setattr__(name, value)

const = Constant()
const.A = 10  # ✅ Allowed
print(const.A)  # Output: 10

# const.A = 12.7  # ❌ TypeError: Cannot modify constant 'A'
```

---

## **📌 6. Python is Case-Sensitive**
Variable names **distinguish between uppercase and lowercase letters**.

### **✅ Example:**
```python
B = 10
b = 20

print(B)  # Output: 10
print(b)  # Output: 20 (Different from B)
```

---

## **📌 7. Taking User Input**
Python allows user input using the `input()` function.

### **🔹 Example:**
```python
x = input("Enter a value: ")  # Takes input as a string
print("You entered:", x)
```

### **🔹 Type Casting (Converting input to a specific type)**
```python
x = int(input("Enter a number: "))  # Converts input to an integer
print("Value:", x, "Type:", type(x))  # Output: Value: 10 Type: <class 'int'>
```

---

## **📌 8. Type Casting (Conversion)**
Python provides built-in functions for type conversion.

### **🛠️ Important Type Conversion Functions:**
| Function | Description |
|----------|------------|
| `int()` | Convert to an integer |
| `float()` | Convert to a float |
| `str()` | Convert to a string |
| `ord()` | Get ASCII value of a character |
| `chr()` | Convert ASCII value to a character |
| `bin()` | Convert to binary |
| `hex()` | Convert to hexadecimal |
| `oct()` | Convert to octal |
| `complex()` | Create complex numbers |

### **🔹 Example:**
```python
x = ord('a')  # Get ASCII value of 'a'
print(x)  # Output: 97

x = chr(97)  # Get character from ASCII value
print(x)  # Output: 'a'

y = bin(10)  # Convert to binary
print(y)  # Output: '0b1010'

z = hex(55)  # Convert to hexadecimal
print(z)  # Output: '0x37'
```

---

## **📌 9. Data Types in Python**
Python supports **primitive and collection data types**.

### **📜 Primitive Data Types:**
- **Integer** → `int`
- **Float** → `float`
- **String** → `str`
- **Complex Number** → `complex`
- **Boolean** → `bool`
- **Bytes** → `bytes`

### **🔹 Example:**
```python
x = complex(2, 4)  # Complex number
print(x)  # Output: (2+4j)

a = True  # Boolean
print(a, type(a))  # Output: True <class 'bool'>

name = "Pawan"  # String
print(name, type(name))  # Output: Pawan <class 'str'>
```

---

## **📌 10. Mutable vs Immutable Data Types**
- **Immutable (Cannot be modified)** → `int`, `float`, `str`, `tuple`, `bytes`
- **Mutable (Can be modified)** → `list`, `set`, `dict`

### **🔹 Example (Immutable String):**
```python
name = "abc"
# name[0] = 'x'  # ❌ TypeError: 'str' object does not support item assignment
print(name)  # Output: 'abc'
```

---

## **📌 11. Collection Data Types**
Python supports **four** main collection data types.

### **📌 List (Ordered, Mutable)**
```python
l = ["Pawan", 1, 3, 56, 78, 90]
print(l)

l[3] = 100  # Modifying an element
print(l)  # Output: ['Pawan', 1, 3, 100, 78, 90]
```

### **📌 Set (Unordered, Unique Elements)**
```python
s = {12, 34, 678, 90, "pawan", 12}  # Duplicate 12 removed
print(s)  # Output: {34, 12, 90, 'pawan', 678}
```

### **📌 Tuple (Ordered, Immutable)**
```python
t = (10, 20, 30)
# t[1] = 50  # ❌ TypeError: 'tuple' object does not support item assignment
print(t)
```

### **📌 Frozenset (Immutable Set)**
```python
fs = frozenset({1, 2, 3, 4})
print(fs)
# fs.add(5)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
```

---

## **🎯 Note :**
✅ **Python is dynamically typed, case-sensitive, and beginner-friendly.**  
✅ **The `print()` function is used for displaying output.**  
✅ **Variables do not need explicit type declaration.**  
✅ **Constants can be created using a custom class.**  
✅ **The `input()` function is used to take user input.**  
✅ **Type conversion functions allow changing data types.**  
✅ **Lists are mutable, while strings and tuples are immutable.**  
✅ **Python collections include lists, sets, tuples, and frozensets.**  

---
