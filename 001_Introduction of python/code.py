
# Introduction of Python
# History of Python


# syntax : 

# print((object(s), [sep=seperation, end = end]))

# object(s) -> string variable of class object

# sep, end -> optional

"""
print("Hello my phython developer..")

print("Hello","Bhai")

print("Hey","Bro","How are you?")


print("Hello","World" , sep="____")
print("Hello","World" , "hey", sep="***")

print("Hello"); print("world")

print("Hello", end="/n"); print("world")

print("Hello", end="***"); print("world")"""




# A = 10

# print(A)

# print(type(A))

# A = 12.7

# print(A)


# In Python, you can't create truly constant variables, but you can enforce immutability using custom classes. Below are different approaches to prevent reassignment.


# class Constant:
#     def __setattr__(self, name, value):
#         if hasattr(self, name):  # If the attribute is already set, prevent reassignment
#             raise TypeError(f"Cannot modify constant '{name}'")
#         super().__setattr__(name, value)

# const = Constant()
# const.A = 10   # ✅ Allowed: First assignment
# print(const.A) # 10

# const.A = 12.7 # ❌ TypeError: Cannot modify constant 'A'

# python case sensitive 


# B = 10

# b = 20

# print(b)
# print(B)



# How to take input from user?

# x = 10
# print(x)


# x = input()

# print(x)
# print("Enter Number : ")
# x = input()

# print(x)

# x = input("Enter Number : ")

# print("Value : ",x)

# Type Casting Constructor


# x = int(input("Enter Number : "))

# print("Value : ",x)
# print(type(x))

"""
1. int()
2. float()
3. str()
4. ord()
5. chr()
6. bin()
7. hex()
8. oct()
9. complex() """

# x = 12

# print(str(x))
# print(type(str(x)) )

# x = ord('a')

# print(x)


# x = chr(97)

# print(x)


# y = bin(10)
# print(y)

# y = bin(5)
# print(y)


# z = hex(55)

# print(z)



# DataType

# 1. primitive datatype -> integer, float, string, complex, bool, bytes

# x = complex(2,4)

# print(x)

# a = True
# print(a)
# print(type(a))

# name = "Pawan"

# print(name)
# print(type(name))


# y = b"Pawan"

# print(y)  # Output: b'Pawan'

# # Attempt to modify an element of bytes
# y[0] = b'H'  # ❌ TypeError: 'bytes' object does not support item assignment

# string

# name = "abc"

# name[0] = 'x'  # ❌ TypeError: 'str' object does not support item assignment

# print(name)


# 2. collection datatype

# 1.list
# 2. set
# 3. tuple
# 4. frozenset



#list -> mutable

# l = ["Pawan",1,3,56,78,90]
# print(l)
# l[3] = 100

# print(l)

#set -> unique , remove dublicate

s = {12,34,678,90,"pawan",12}

print(s) 