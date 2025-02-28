### Python Lecture Notes: Understanding Functions, Reflection, and Inheritance

---

### **1. Nested Functions**

A **nested function** is a function that is defined inside another function. Nested functions help in encapsulating functionality, making your code cleaner and more organized. A nested function can access variables and functions from the outer function.

#### Example:
```python
def outer():
    print("Call Outer function")
    
    def inner():
        print("Call Inner function")
        
        def i2():
            print("Call most inner function")
        
        i2()
    
    inner()

# Call the outer function
outer()
```

**Explanation**:
- In the example above, we define an outer function `outer()`, which contains an inner function `inner()`, and the inner function contains another function `i2()`. 
- The innermost function `i2()` is only accessible within the `inner()` function. Similarly, `inner()` is only accessible within `outer()`.
- **Note**: We can call the nested functions only within the scope of the outer function.

---

### **2. Reflection-Enabling Functions**

Reflection in Python allows you to inspect and manipulate the structure of an object during runtime. Python provides several built-in functions to enable reflection.

#### **1. `type()`**
The `type()` function is used to check the data type of a variable. 

```python
a = (3, 4, 5)
print(type(a))  # Output: <class 'tuple'>
```

**Explanation**: The `type()` function tells us that the variable `a` is of type `tuple`.

---

#### **2. `dir()`**
The `dir()` function is used to check which operations (methods and attributes) can be performed on an object.

```python
a = (3, 4, 5)
print(dir(a))
```

**Explanation**: The `dir()` function lists all the methods and properties associated with the object `a`. This includes the built-in functions like `append()`, `remove()`, etc.

---

#### **3. `callable()`**
The `callable()` function checks whether an object is callable (i.e., whether it can be executed as a function).

```python
def hi():
    print("Hello")

if callable(hi):
    hi()  # Output: Hello

x = 8
print(callable(x))  # Output: False
```

**Explanation**: In this example:
- `hi()` is callable, so `callable(hi)` returns `True`.
- `x` is not callable (it is an integer), so `callable(x)` returns `False`.

---

#### **4. `isinstance()`**
The `isinstance()` function checks if an object is an instance of a specific class or a subclass.

```python
class Student:
    name = None
    age = None

s1 = Student()
print(isinstance(s1, Student))  # Output: True

print(isinstance(42, Student))  # Output: False
```

**Explanation**:
- `isinstance(s1, Student)` checks if `s1` is an instance of the `Student` class. It returns `True`.
- `isinstance(42, Student)` checks if `42` is an instance of the `Student` class. It returns `False`.

---

#### **5. `getattr()`**
The `getattr()` function is used to check if an object has a specific attribute. If the attribute exists, it returns its value; if not, it raises an error (unless you specify a default value).

```python
class Student:
    name = "Utkarsh"
    age = 20

s1 = Student()
print(getattr(s1, "name"))  # Output: Utkarsh
print(getattr(s1, "subject", "Not Available"))  # Output: Not Available
```

**Explanation**:
- `getattr(s1, "name")` returns `"Utkarsh"` because the `name` attribute exists in the class `Student`.
- `getattr(s1, "subject", "Not Available")` returns `"Not Available"` because the `subject` attribute does not exist in the class.

---

### **3. Inheritance in Python**

Inheritance allows a class to inherit the attributes and methods of another class. This helps in code reuse and creating a hierarchical relationship between classes.

#### **1. Simple / Single Inheritance**

In **simple inheritance**, one class (child class) inherits the properties and methods of a single parent class.

```python
class A:
    name = "Utkarsh"
    school = "Best"

class B(A):  # Inherits from class A
    pass

o1 = B()
print(o1.name, o1.school)  # Output: Utkarsh Best
```

**Explanation**: 
- In this example, class `B` inherits the attributes `name` and `school` from class `A`.
- The child class `B` can access all properties and methods of class `A` (but cannot modify them unless explicitly done).

---

#### **2. Multilevel Inheritance**

In **multilevel inheritance**, a class inherits from another class, which itself is derived from another class, forming a chain of inheritance.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def get(self):
        print("Hello from B")

class C(B):
    def disp(self):
        print("Hello from C")

o1 = C()
o1.disp()  # Output: Hello from C
o1.get()   # Output: Hello from B
o1.hello() # Output: Hello from A
```

**Explanation**:
- Class `A` has a method `hello()`.
- Class `B` inherits from class `A` and adds a method `get()`.
- Class `C` inherits from class `B` and adds a method `disp()`.
- An object of class `C` can access all the methods from `A`, `B`, and `C`.

---

#### **3. Multiple Inheritance**

In **multiple inheritance**, a class inherits from more than one class, meaning it can inherit attributes and methods from multiple parent classes.

```python
class A:
    def hello(self):
        print("Hello from A")

class B:
    def get(self):
        print("Hello from B")

class C(A, B):  # Inherits from both A and B
    pass

o1 = C()
o1.hello()  # Output: Hello from A
o1.get()    # Output: Hello from B
```

**Explanation**:
- Class `C` inherits from both class `A` and class `B`.
- The object `o1` can access methods from both classes `A` and `B`.

---

#### **4. Hierarchical Inheritance**

In **hierarchical inheritance**, multiple child classes inherit from a single parent class.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    pass

o1 = B()
o1.hello()  # Output: Hello from A

o2 = C()
o2.hello()  # Output: Hello from A
```

**Explanation**:
- Both `B` and `C` inherit from class `A`.
- Both `o1` and `o2` can access the method `hello()` from class `A`.

---

#### **5. Hybrid Inheritance**

**Hybrid inheritance** is a combination of two or more types of inheritance, such as single, multiple, or multilevel inheritance.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C:
    def hi(self):
        print("Hello from C")

class D(B, C):
    pass

o1 = D()
o1.hello()  # Output: Hello from A
o1.greet()  # Output: Hello from B
o1.hi()     # Output: Hello from C
```

**Explanation**:
- Class `D` inherits from both class `B` (which inherits from `A`) and class `C`.
- `o1` can access methods from all its parent classes (`A`, `B`, and `C`).

---
