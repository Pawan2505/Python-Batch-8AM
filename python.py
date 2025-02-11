# a = 10

# print(a)

# a = 5 # int
# b = 3.7 # float
# c = 'Hello' # str
# d = "Hello" # str
# e = '''Hello
# Python''' # multi-line string
# f = True # bool
# g = (4 + 2j) # complex

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)


# Collection Datatypes

# l = [3, 6, 7.9, True, 3, 6] # list - mutable
# l[1] = 99
# t = (5, 2, 9) # tuple - immutable
# # t[0] = 45  # not ok
# s = {2, 4, 8, 2, 6, 4} # set - mutable
# f = frozenset({2, 3, 5, 7, 2, 5}) # immutable => dublicate
# d = {'id': 1, 'name': 'Rahul', 'age': 20} # dict - mutable

# d['age'] = 44

# # d['name'] = 'Manish'

# d.update({'name':"Pawan",'age':990})

# print(l)
# print(t)
# print(s)
# print(f)
# print(d)


# 1. Convert Tuple to List and Modify
# Since lists are mutable, you can convert the tuple to a list, modify the value, and convert it back to a tuple.

# t = (5, 2, 9)  # Tuple (immutable)

# # Convert to list
# temp_list = list(t)

# # Modify the value (e.g., change 2 to 7)
# temp_list[1] = 7

# # Convert back to tuple
# t = tuple(temp_list)

# print(t)


# In Python, a frozenset is an immutable version of a set, meaning its elements cannot be changed after creation. However, just like a normal set, a frozenset does not allow duplicate values.

# f = frozenset({2, 3, 5, 7, 2, 5})  # Duplicate values included
# print(f)


# marks = int(input("Enter Number :"))

# print("Marks : ",marks)


# marks = float(input("Enter Number :"))

# print("Marks : ",marks)


#int 
#float
#string
#boolean

# In Python, there are several built-in data types, categorized as follows:

# ### 1. **Numeric Types**
#    - `int` → Integer (e.g., `10`, `-5`)
#    - `float` → Floating-point number (e.g., `10.5`, `-3.14`)
#    - `complex` → Complex numbers (e.g., `2 + 3j`, `-1j`)

# ### 2. **Sequence Types**
#    - `str` → String (e.g., `"Hello"`, `'Python'`)
#    - `list` → List (e.g., `[1, 2, 3]`, `["apple", "banana"]`)
#    - `tuple` → Tuple (e.g., `(1, 2, 3)`, `("red", "blue")`)
#    - `range` → Range (e.g., `range(5)` → `0,1,2,3,4`)

# ### 3. **Set Types**
#    - `set` → Unordered collection of unique items (e.g., `{1, 2, 3}`)
#    - `frozenset` → Immutable set (e.g., `frozenset({1, 2, 3})`)

# ### 4. **Mapping Type**
#    - `dict` → Dictionary (key-value pairs) (e.g., `{"name": "Alice", "age": 25}`)

# ### 5. **Boolean Type**
#    - `bool` → Boolean (`True`, `False`)

# ### 6. **Binary Types**
#    - `bytes` → Immutable sequence of bytes (e.g., `b"Hello"`)
#    - `bytearray` → Mutable sequence of bytes (e.g., `bytearray(5)`)
#    - `memoryview` → Memory view object (e.g., `memoryview(b"Hello")`)

# ### 7. **None Type**
#    - `NoneType` → Represents absence of value (`None`)

# ### Summary:
# Python has **14** fundamental data types categorized under different types. Let me know if you need further clarification! 🚀


# a = `b"Manish"`

# print(a)  // Output :  b'Manish'



# b =10
# c=10

# a = bool(b==c)

# print(a)  // output : True



# name = input("Enter Name : ")

# print(name)  // Pawan

# Method :1
'''
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")

print(f'Hello, My name is {name}, I am {age} years old, and I belong to {address}.')'''


#Method : 2

'''  
name = input("Enter Name: ")
age = int(input("Enter Age: "))
address = input("Enter Address: ")

print("Hello, My name is {}, I am {} years old, and I belong to {}.".format(name, age, address))

'''

#  Floor Divide and Assign (//=) in Python -> complete quosent -> remove de

# a = 17
# b = 3

# a //= b  # Equivalent to a = a // b

# print(a)  # Output: 5


# a = -19
# b = 3

# a //= b  

# print(a)  # Output: -7  (answer -> if value in decimal then it increase by one)

# a = 19
# b = 3

# a //= b  

# print(a)  # Output: 6  (answer -> if value in decimal then it decrease by one)


"""

Your concept is **partially correct**, but let's clarify it completely.  

### **Correct Concept for Floor Division (`//`)**
- **Floor division (`//`) always rounds down to the nearest lower integer** (not necessarily increasing or decreasing by 1).
- The rounding follows the **mathematical floor function**:
  - For **positive numbers**, it behaves like normal integer division.
  - For **negative numbers**, it rounds further **down** (away from zero).

---

### **Corrected Explanation of Your Code:**
```python
a = -19
b = 3

a //= b  

print(a)  # Output: -7  ✅
```
✔ **Explanation:**
- `-19 ÷ 3 = -6.3333...`
- Floor division **rounds down** to the nearest lower integer → `-7` (not `-6`).

---

```python
a = 19
b = 3

a //= b  

print(a)  # Output: 6  ✅
```
✔ **Explanation:**
- `19 ÷ 3 = 6.3333...`
- Floor division **rounds down** to `6` (not `5`).

---

### **Final Concept:**
- **For positive numbers** → `//` rounds **down**, but the value decreases only if the result is not already an integer.
- **For negative numbers** → `//` rounds **further down** (away from zero), making the number **more negative**.

Would you like more examples? 😊🚀

"""



# Membership Operators

# Example 1: Using in with a List

# lst = [1, 2, 3, 4, 5]

# print(3 in lst)   # Output: True
# print(10 in lst)  # Output: False


# ✅ Explanation:

# 3 in lst → ✅ True (since 3 is in the list)
# 10 in lst → ❌ False (since 10 is not in the list)



# Example 2: Using not in with a List


# lst = [1, 2, 3, 4, 5]

# print(6 not in lst)  # Output: True
# print(2 not in lst)  # Output: False

# ✅ Explanation:

# 6 not in lst → ✅ True (since 6 is not in the list)
# 2 not in lst → ❌ False (since 2 is in the list)


# Example 3: Using in and not in with a String

# text = "Hello, World!"

# print("Hello" in text)      # Output: True
# print("Python" not in text) # Output: True


# ✅ Explanation:

# "Hello" in text → ✅ True (Hello exists in the string).
# "Python" not in text → ✅ True (Python is not in the string).


# Example 4: Using in with a Tuple


# tup = (10, 20, 30, 40)

# print(20 in tup)   # Output: True
# print(50 in tup)   # Output: False


# ✅ Explanation:

# 20 in tup → ✅ True (20 exists in the tuple).
# 50 in tup → ❌ False (50 is not in the tuple).




# Example 5: Using in with a Dictionary (Keys Only)

# person = {"name": "Pawan", "age": 25, "city": "Azamgarh"}

# print("name" in person)      # Output: True
# print("country" not in person)  # Output: True


# ✅ Explanation:

# "name" in person → ✅ True (name is a key in the dictionary).
# "country" not in person → ✅ True (country is not a key in the dictionary).


# Identity Operators (is, is not) in Python

# Example 1: Using is with Immutable Types (Integers)

# x = 5
# y = 5  # Small integers (-5 to 256) are stored in the same memory location

# print(x is y)  # Output: True


# ✅ Explanation:

# Python caches small integers (-5 to 256), so x and y share the same memory address.


# Example 2: Using is not with Lists (Mutable Types)

# a = [1, 2, 3]
# b = [1, 2, 3]  # Even though the values are the same, they are stored in different memory locations

# print(a is not b)  # Output: True

# ✅ Explanation:

# Lists are mutable, so a and b have different memory addresses, even though their values are the same.


# Example 3: Using is with Strings (Immutable)

# s1 = "hello"
# s2 = "hello"

# print(s1 is s2)  # Output: True

# ✅ Explanation:

# Python optimizes memory for short strings, so s1 and s2 share the same memory address.

# Example 4: Using is with None

# x = None
# y = None

# print(x is y)  # Output: True

# ✅ Explanation:

# None is a singleton object in Python, so all None variables refer to the same memory location.



# Example 5: Difference Between == and is

# list1 = [10, 20, 30]
# list2 = [10, 20, 30]

# print(list1 == list2)  # Output: True  (Values are the same)
# print(list1 is list2)  # Output: False (Different memory locations)


# ✅ Explanation:

# == checks values → ✅ True
# is checks memory locations → ❌ False



# a = 10
# b = 5

# # Arithmetic Operators
# print(a + b)  # Output: 15

# # Comparison Operators
# print(a > b)  # Output: True

# # Logical Operators
# print(a > 5 and b < 10)  # Output: True

# # Bitwise Operators
# print(a & b)  # Output: 0

# # Assignment Operators
# a += b
# print(a)  # Output: 15

# # Identity Operators
# x = [1, 2, 3]
# y = x
# print(x is y)  # Output: True

# # Membership Operators
# print(3 in x)  # Output: True


# # Logical Operators
# print(a > 5 or b < 1)  # Output: True


# true_part if condition else false_part

# a = 20
# b = 102

# print("A Greater") if a>b else print("B greater")


# marks > 80  -> marks >=90 -> A+ grade, marks < 90 -> A Grade


# marks = 75

# print("A+ Grade") if marks >=90 else print("A Grade") if marks >= 80 else print("You are not eligible")


# num = 1
# while num<=10:
#   print(num)
#   # num = num+1
#   num+=1

# num = 10
# while num>=1:
#   print(num)
#   # num = num+1
#   num-=1




# print(list(range(10)))

# print(set(range(10)))

# print(tuple(range(10)))

# range(1, 11) 

# print(list(range(1,11)))
# print(list(range(3,11)))

# range(start, end, step)

# print(list(range(3,11,7)))  #[3, 10]


# for loop

'''
for var in sequence:
    body
'''

# for i in range(1,11) :
#   if i%2 == 0:
#     print(i)
