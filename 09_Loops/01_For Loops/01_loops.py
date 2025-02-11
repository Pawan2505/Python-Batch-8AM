# 🚀 Loops in Python

# ✅ 1. For Loop (Iterating over a range)
print("Using for loop:")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# ✅ 2. For Loop with Step Value
print("For loop with step:")
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9

# ✅ 3. Iterating Over a List
fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)

# ✅ 4. While Loop (Executing Until Condition Becomes False)
count = 1

while count <= 5:
    print("Count:", count)
    count += 1  # Increment

# ✅ 5. Infinite While Loop (Stopped using Break)
x = 1
while True:
    print(x)
    x += 1
    if x > 5:
        break  # Stops the loop

# ✅ 6. Using Continue in a Loop
print("Skipping 3 using continue:")
for i in range(1, 6):
    if i == 3:
        continue  # Skips 3
    print(i)  # Output: 1 2 4 5

# ✅ 7. Using Else with Loop
print("Using else with loop:")
for i in range(5):
    print(i)
else:
    print("Loop finished!")  # Executed when loop completes normally

# ✅ 8. Nested Loops (Loop inside another loop)
print("Nested loops example:")
for i in range(1, 4):  # Outer Loop
    for j in range(1, 4):  # Inner Loop
        print(f"({i}, {j})", end=" ")
    print()
