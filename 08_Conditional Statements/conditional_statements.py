# 🚀 Conditional Statements in Python

# ✅ if statement
age = 20

if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.

# ✅ if-else statement
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ✅ if-elif-else statement (Multiple Conditions)
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# ✅ Nested if statement
x = int(input("Enter a number: "))

if x > 0:
    print("Positive Number")
    if x % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Negative Number or Zero")
