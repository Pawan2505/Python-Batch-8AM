## **Lecture Notes: Understanding Classes and Objects in Python**

### **1. What is a Class?**
A **class** is like a blueprint or template that defines how objects should behave. It contains:
- **Attributes**: The properties or characteristics of an object.
- **Methods**: The functions that define the behavior of the object.

### **2. What is an Object?**
An **object** is an instance of a class. It is created using the class blueprint. Once you have a class, you can create as many objects as you need from it.

- A class is the **blueprint**.
- An object is an **actual instance** created from the class.

---

### **3. Syntax of Class and Object**

```python
class ClassName:
    # 1. Attributes (Properties/Variables)
    # 2. Methods (Functions)
    # 3. Constructor (__init__)
    # 4. Destructor (__del__)

# Creating an object from the class
object_name = ClassName()
```

---

### **4. Example: Class and Object**

Here, we create a `Pokemon` class with some attributes and methods. Then, we create objects (like `Pikachu` and `Bulbasaur`) from the `Pokemon` class.

#### **1. Class with Attributes and Methods**

```python
class Pokemon:
    # Attributes of the class
    name = "pikachu"
    ptype = "Electric"
    health = 70

    # Method to display details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Ptype: {self.ptype}")
        print(f"Health: {self.health}")

# Creating an object from the class
Pikachu = Pokemon()  # Pikachu is an object of the class Pokemon

# Calling the method to display details
Pikachu.display()
```

- **Class**: `Pokemon`
- **Object**: `Pikachu`
- **Method**: `display()` is a function defined in the class, which prints the object's details.

---

### **5. How to Create and Use Objects**

- To create an **object**, simply call the class like a function:

```python
Pikachu = Pokemon()  # Creating an object from the class
```

- After creating an object, you can access the attributes and methods using the **dot (`.`) operator**:

```python
Pikachu.name  # Accessing the 'name' attribute of the object Pikachu
Pikachu.display()  # Calling the 'display()' method of the object Pikachu
```

---

### **6. Compile-time Initialization in Class**

- You can initialize class attributes directly inside the class itself.

```python
class Pokemon:
    name = "pikachu"
    ptype = "Electric"
    health = 70

Pikachu = Pokemon()  # Pikachu is an object of the class Pokemon

# Printing the values for Pikachu object
print("Name:", Pikachu.name)
print("Ptype:", Pikachu.ptype)
print("Health:", Pikachu.health)
```

Here, we initialize the attributes inside the class, and whenever we create an object like `Pikachu`, it automatically gets these values.

---

### **7. Manual Initialization (Setting Values after Object Creation)**

You can create an object and later assign values to its attributes.

```python
class Pokemon:
    name = None
    ptype = None
    health = None

Pikachu = Pokemon()  # Creating the object

# Manually initializing the values for Pikachu
Pikachu.name = "pikachu"
Pikachu.ptype = "Electric"
Pikachu.health = 70

# Printing values of Pikachu
print("Name:", Pikachu.name)
print("Ptype:", Pikachu.ptype)
print("Health:", Pikachu.health)
```

In this case, we created the `Pikachu` object first and then manually assigned values to its attributes.

---

### **8. Run-time Initialization (User Input for Attributes)**

You can also take input from the user to set the values for the object attributes.

```python
class Student:
    sid = None
    name = None
    age = None

# Creating two student objects
s1 = Student()
s2 = Student()

# Taking input for the first student object (s1)
s1.sid = int(input("Enter Student ID for s1: "))
s1.name = input("Enter Student Name for s1: ")
s1.age = int(input("Enter Student Age for s1: "))

# Taking input for the second student object (s2)
s2.sid = int(input("Enter Student ID for s2: "))
s2.name = input("Enter Student Name for s2: ")
s2.age = int(input("Enter Student Age for s2: "))

# Print the details for both student objects
print(f"Student 1 - ID: {s1.sid}, Name: {s1.name}, Age: {s1.age}")
print(f"Student 2 - ID: {s2.sid}, Name: {s2.name}, Age: {s2.age}")
```

---

### **9. Using Getter and Setter Methods**

- **Getter** methods are used to get (retrieve) values of the object's attributes.
- **Setter** methods are used to set (modify) values of the object's attributes.

```python
class Student:
    sid = None
    name = None
    age = None

    # Setter method to set values
    def setData(self, i, n, a):
        self.sid = i
        self.name = n
        self.age = a

    # Getter method to get values
    def getData(self):
        print(f"ID: {self.sid}, Name: {self.name}, Age: {self.age}")

# Creating two student objects
s1 = Student()
s2 = Student()

# Using setter methods to set data for s1 and s2
s1.setData(1, "Utkarsh", 20)
s2.setData(2, "Pawan", 25)

# Using getter methods to display data for s1 and s2
s1.getData()
s2.getData()
```

### **Note:**

- **Class**: A class is a blueprint that defines the properties (attributes) and behaviors (methods) of objects.
- **Object**: An object is an instance of a class, created using the class's blueprint. 
- **Constructor** (`__init__`): Used to initialize an object's attributes when it is created.
- **Methods**: Functions defined in a class to perform actions or return information.
- **Getter and Setter Methods**: Special methods used to safely access and modify object attributes.

### **Important Tips:**

1. **Class Name**: Always start the class name with a capital letter.
2. An **object** is created from a class by calling the class name.
3. Use the **dot (`.`) operator** to access attributes and methods of an object.
4. You can initialize class attributes **before** or **after** creating an object, depending on the situation.

---
