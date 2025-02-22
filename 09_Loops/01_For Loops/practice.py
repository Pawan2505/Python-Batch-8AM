# ---- FOR LOOP ----

# Basic structure of a for loop
# for variable in sequence:
#     #code

# List of numbers
l = [11, 22, 33, 44, 55, 66]

# Loop through the list and print each item
for item in l:
    print(item)


# Loop through a range (0 to 4)
for i in range(5):
    print(i)

# Print the range object itself
print(range(5))


# Loop through each character in a string
name = "Pawan"
for char in name:
    print(char)


# Demonstrating the 'else' block with a for loop
for num in range(5):
    print(num)
else:
    print("Loop Completed")


# Using 'break' to exit the loop when a condition is met
for num in range(5):
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)


# Using 'continue' to skip an iteration when a condition is met
for num in range(5):
    if num == 3:
        continue  # Skip this iteration when num is 3
    print(num)
else:
    print("Loop Completed")


# Taking multiple inputs using a for loop
n = int(input("Enter the number of elements: "))
number = []

# Collect 'n' numbers from the user and append to the list
for i in range(n):
    num = int(input(f"Enter number {i}: "))
    number.append(num)

# Display the entered numbers
print("You entered:", number)

# Find the index of the number 25 in the list
print(number.index(25))  # Example assuming 25 exists in the list


# Taking multiple inputs with a reverse range
n = int(input("Enter the number of elements: "))
number = []

# Loop with a range from 10 down to 6
for i in range(10, 5, -1):
    num = int(input(f"Enter number {i}: "))
    number.append(num)

# Display the entered numbers
print("You entered:", number)

# Find the index of the number 25 in the list
print(number.index(25))  # Example assuming 25 exists in the list


# ---- FORMAT METHODS ----

# Using .format() for string formatting
num = 34
# Example of formatting using positional arguments
print("The value of num is {}.".format(num))

# Positional Arguments with .format()
print("My name is {} and I am {} years old".format("Pawan", 24))

# Named Arguments with .format()
print("My name is {name} and I am {age} years old".format(name="Pawan", age=24))

# Formatting numbers with .format()
print("The price is {:.1f} rupees".format(2534.63982578))


# ---- WHILE LOOP ----

# Basic structure of a while loop
# while condition:
#     #code to execute 

# Example of a simple while loop with a counter
count = 1
while count <= 10:
    print(count)
    count += 1  # Increment counter


# While loop with an else block
count = 1
while count <= 10:
    print(count)
    count += 1
else:
    print("Loop ended")


# While loop with a 'break' to exit early
count = 1
while count <= 10:
    if count == 5:
        break  # Exit the loop when count is 5
    print(count)
    count += 1
else:
    print("Loop ended")  # This won't execute because the loop is broken


# While loop with 'continue' to skip an iteration
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Skip the iteration when count is 5
    print(count)


# While loop with an external countdown timer
import time

countdown = 5
while countdown > 0:
    print("Time left:", countdown)
    time.sleep(2)  # Pause the execution for 2 seconds
    countdown -= 1
print("Time's up!")
