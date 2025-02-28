'''
1. Nested Function 
2. Reflection Enabling Function
   1. type()
   2. dir()
   3. callable
   4. isinstance()
   5. getattr()

3. Inheritnce 
   1. simple / single inheritance 
   2. multilevel inheritance
   3. multiple inheritnce 
   4. hierarchial inheritance 
   5. hybrid inheritance

'''


#1. #Nested function

# def outer():
#     print("Call Outer function")
#     def inner():
#         print("call inner function")
#         def i2():
#             print("call most inner Function")
#         i2()
#     inner()
# outer()

# #we can call the function in that scope only .


#2. #Reflection enabling function 

#1. type() : This function is used to konw the datatype of  any veriable.

# a=(3,4,5)
# print(type(a))

#2. dir()  : This function is used to konw what kind of operation can we can perform in the veriable.

# a=(3,4,5)
# print(dir(a))

#3. callable() : This Function is used to konw whether the function is callable or not .

# def hi():
#     print("Hello")

# if(callable(hi)):  # This function is callable so it gives True
#     hi()

# x = 8

# print(callable(x)) # This function is not callable so it gives Flase

#4. isinstance() : This function is used to know whether the object is present in the class or not.

# class student:
#     name = None
#     age =None

# s1 = student()

# print(isinstance(s1,student)) # If object is pesent it gives True

# print(isinstance(42,student)) # If object is not pesent it gives False

#5. getattr() : This function is used to know whether the Attribute is present in the class or not.

# class student:
#     name = "utkarsh"
#     age =20

# s1 = student()

# print(s1.name)
# print(getattr(s1,"name"))  # both is used to print .
# print(getattr(s1,"subject"))  # This will give AttributeError: 'student' object has no attribute 'subject'.

#3. Inheritance 

#1. Simple / single Inheritance

# class A:
#     name = "utkarsh"
#     school = "Best"

# class B(A):  #inherit the properties of class A in class B.
#     pass

# o1 = B()

# print(o1.name , o1.school) # Printing the Output
# print(o1.name , o1.school,o1.age) #AttributeError: 'B' object has no attribute 'age'

# we are giving properties to Class B 

# class A:
#     name = "utkarsh"
#     school = "Best"

# class B(A):  #inherit the properties of class A in class B and also give properties to class B.
#     age = 20

# o1 = B()

# print(o1.name , o1.school,o1.age)  

#2. Multilevel Inheritance

# # Class A with a method 'hello'
# class A:
#     def hello(self):
#         print("Hello from A")

# # Class B inherits from A and adds a method 'get'
# class B(A):
#     def get(self):
#         print("Hello from B")

# # Class C inherits from B and adds a method 'disp'
# class C(B):
#     def disp(self):
#         print("Hello from C")  # Changed message to reflect class C

# # Creating an object of class C
# o1 = C()

# # Calling the methods   
# o1.disp()   # Output: Hello from C
# o1.get()    # Output: Hello from B
# o1.hello()  # Output: Hello from A