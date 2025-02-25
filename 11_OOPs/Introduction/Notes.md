## **Lecture Notes: Understanding Classes in Python**

### **1. What is a Class?**
In Python, a **class** is like a blueprint for creating objects. It defines the structure and behavior of objects that belong to that class.

- **Class Name**: Always start the class name with a capital letter. For example, `Pokemon`, `Student`, etc.
- **Attributes (Properties)**: These are the variables that store data for the class. They represent the characteristics of an object.
- **Methods (Functions)**: These are the functions defined inside a class. They define the behavior of the objects.
- **Constructor**: This is a special function called `__init__()` used to initialize the object's attributes when it's created.
- **Destructor**: This is a special function called `__del__()` used to clean up when the object is destroyed (not often used in Python).

---

### **2. Syntax of Class**

```python
class ClassName:
    # 1. Attributes (Properties/Variables)
    # 2. Methods (Functions)
    # 3. Constructor (__init__)
    # 4. Destructor (__del__)
```

### **3. Example: Class with Attributes and Methods**

#### **1. Compile-time Initialization**
In compile-time initialization, you initialize the attributes directly inside the class itself.

```python
class Pokemon:
    name = "pikachu"  # attribute initialized
    ptype = "Electric"
    health = 70

Pikachu = Pokemon()  # Pikachu is an object of the class Pokemon

# Print the values of Pikachu
print("Name:", Pikachu.name)
print("Ptype:", Pikachu.ptype)
print("Health:", Pikachu.health)
```

---

#### **2. Compile-time Initialization with Manual Input**
In this method, we initialize the attributes as `None` initially, and later set their values.

```python
class Pokemon:
    name = None  # attributes initialized with None
    ptype = None
    health = None

Pikachu = Pokemon()  # Pikachu is an object of the class Pokemon

# Manually set values for Pikachu
Pikachu.name = "pikachu"
Pikachu.ptype = "Electric"
Pikachu.health = 70

# Print the values for Pikachu
print("Name:", Pikachu.name)
print("Ptype:", Pikachu.ptype)
print("Health:", Pikachu.health)

# Create another object Bulbasaur
Bulbasaur = Pokemon()

# Manually set values for Bulbasaur
Bulbasaur.name = "Bulbasaur"
Bulbasaur.ptype = "Water"
Bulbasaur.health = 75

# Print the values for Bulbasaur
print("Name:", Bulbasaur.name)
print("Ptype:", Bulbasaur.ptype)
print("Health:", Bulbasaur.health)
```

---

#### **3. Run-time Initialization (User Input)**
This is when you take input from the user to set the values of attributes.

```python
class Student:
    sid = None
    name = None
    age = None

# Creating two student objects
s1 = Student()
s2 = Student()

# Taking input for student s1
s1.sid = int(input("Enter Student ID for s1: "))
s1.name = input("Enter Student Name for s1: ")
s1.age = int(input("Enter Student Age for s1: "))

# Taking input for student s2
s2.sid = int(input("Enter Student ID for s2: "))
s2.name = input("Enter Student Name for s2: ")
s2.age = int(input("Enter Student Age for s2: "))

# Print the details of both students
print(f"Student 1 - ID: {s1.sid}, Name: {s1.name}, Age: {s1.age}")
print(f"Student 2 - ID: {s2.sid}, Name: {s2.name}, Age: {s2.age}")
```

---

#### **4. Using Getter and Setter Methods**
In this approach, we use **getter** and **setter** methods to access and modify the attributes.

- **Setter method**: This method sets the values of the attributes.
- **Getter method**: This method retrieves and displays the values of the attributes.

```python
class Student:
    sid = None
    name = None
    age = None

    # Setter method to set data
    def setData(self, i, n, a):
        self.sid = i
        self.name = n
        self.age = a

    # Getter method to get data
    def getData(self):
        print(f"ID: {self.sid}, Name: {self.name}, Age: {self.age}")

# Create two student objects
s1 = Student()
s2 = Student()

# Using setter methods to set data
s1.setData(1, "Utkarsh", 20)
s2.setData(2, "Pawan", 25)

# Using getter methods to display data
s1.getData()
s2.getData()
```

---

### **Note:**

- A **class** is a blueprint for creating objects.
- **Attributes** are the properties of the class (variables).
- **Methods** define the behavior of the class (functions).
- **Constructor** (`__init__`) initializes the object when created.
- **Destructor** (`__del__`) cleans up the object when it’s destroyed.
- You can initialize class attributes at compile-time, manually, or through user input during runtime.
- **Getter** and **Setter** methods are used to safely access and modify attributes.

---

### **Important Tips:**

1. Remember, **class names** should always start with a capital letter (e.g., `Pokemon`, `Student`).
2. You can initialize class attributes in multiple ways: at compile-time, manually, or during runtime.
3. **Getter and Setter** methods are a good practice to ensure controlled access to class attributes.
4. Always use **`self`** inside methods to refer to instance variables.

---

