'''
Polymorphism and It's types.

'''


#Method Overloading 

#class => Multiple Methods
#      => Same names , But different arguments.

# class A:
#     def truck(self):
#         print("Empty truck is running.")

#     def truck(self, n):
#         print("truck s running with ", n)

# o1 = A()
# # o1.truck()
# o1.truck(30)


#method overriding 

#Inheritance => Multiple class => Multiple Methods
#            => Same name , Arguments same

# class India:
#     def person(self):
#         print("Myself Utkarsh.")
#         print ("I am Indian.")
#         print("I am Wearing dhoti and khadi.")


# class Canada(India):
#     def person(self):
#         print("Myself Utkarsh.")
#         print ("I am Canadian.")
#         print("I am Wearing Jeans and T-shirt")

# # o1 = Canada()  # child class have more priority than the parent class if we make the object of child class.
# # o1.person()
# o1 = India()  # parent class have more priority than the child class if we make the object of parent class.
# o1.person()


class complex:
    def __init__(self, n1 ,n2):
        self.x =n1
        self.y =n2

    def __add__(self,n):
        p =self.x + n.x
        q =self.y + n.y
        return complex(p,q)
    
    def getData(self):
        print(f"x={self.x}  & y={self.y}")


c1 = complex(5,3)
c2 = complex(1,6)

c1.getData()
c2.getData()

c3 = c1 + c2
 
c3.getData()