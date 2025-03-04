    '''
First letter of class is always capital

syntax :

class Class_name:
    1. attributes | properties | veriables
    2. methods | function
    3. constructor
    4. Destructor
'''
# compile-time initialization (in class)

# class Pokemon:
#     name ="pikachu"   # we initialized the attributes 
#     ptype ="Electric"
#     health =70

# Pikachu = Pokemon() # Pikachu is the object of the class Pokemon 

# #printig the values for pikachu

# print("Name : ",Pikachu.name )
# print("ptype : ",Pikachu.ptype )
# print("health : ",Pikachu.health )

# compile-time initialization (Manual Input) 


# class Pokemon:
#     name =None   # we have to initialized the attributes with None value , otherwise it will give error
#     ptype =None
#     health =None

# Pikachu = Pokemon() # Pikachu is the object of the class Pokemon 

# #initialized the values  for pikachu

# Pikachu.name = "pikachu"
# Pikachu.ptype = "Electric"
# Pikachu.health = 70

# #printig the values for pikachu

# print("Name : ",Pikachu.name )
# print("ptype : ",Pikachu.ptype )
# print("health : ",Pikachu.health )


# Bulbasaur = Pokemon() # Bulbasaur is the another object of the class Pokemon 

# #initialized the values for Bulbasaur

# Bulbasaur.name = "Bulbasaur"
# Bulbasaur.ptype = "Water"
# Bulbasaur.health = 75

# #printig the values for Bulbasaur
 
# print("Name : ",Bulbasaur.name )
# print("ptype : ",Bulbasaur.ptype )
# print("health : ",Bulbasaur.health )


# Run-time initialization (User's Input) 

# class student:  
#     sid =None
#     name =None
#     age =None

# s1 = student() # s1 is the another object of the class Student 
# s2 = student() # s2 is the another object of the class Student

# #Taking input for the s1 object

# s1.sid = int(input("Enter Student ID : "))
# s1.name = ("Enter Student Name : ")
# s1.age = int(input("Enter student age : "))

# #Taking input for the s2 object

# s2.sid = int(input("Enter Student ID : "))
# s2.name = ("Enter Student Name : ")
# s2.age = int(input("Enter student age : "))

# print(f"Id {s1.sid} name{s1.name} age {s1.age}") #printing Output for s1 object 
# print(f"Id {s2.sid} name{s2.name} age {s2.age}") # printing Output for s2 object 


# Taking inputa from the users Using Getter and Setter Method

# class student:
#     sid =None
#     name =None
#     age =None

# #setter method

#     def setData(self,i,n,a):
#         self.sid = i
#         self.name = n
#         self.age = a

# #Getter method 

#     def getData(self):
#         print(self.sid, self.name, self.age)

# s1 = student() # creating objects
# s2 = student()

# s1.setData(1,"utkarsh",20)   #SetData using setter method
# s2.setData(2,"pawan",25)   

# s1.getData()  #Printing Data using Getter mathod
# s2.getData()