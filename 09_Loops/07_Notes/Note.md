# **Lecture Notes: Loops in Python**

## **Introduction to Loops**

A loop is a programming structure that repeats a block of code multiple times based on a condition. It allows us to perform repetitive tasks without needing to write the same code repeatedly. Loops are crucial for many programming tasks, such as processing items in a list or counting occurrences.

In Python, there are two main types of loops:
- **For Loop**
- **While Loop**

### **Why Loops?**
Loops help in:
1. **Reducing Code Duplication**: Instead of writing the same code multiple times, loops help you automate repetition.
2. **Iterating Over Sequences**: With loops, we can process each element in a list, string, tuple, etc.
3. **Handling Dynamic Data**: Loops can work with data of varying sizes, like processing user input or reading data from a file.

---

## **1. For Loop**

The `for` loop is used to iterate over a sequence (such as a list, string, range, etc.) and execute a block of code for each item in the sequence. The loop continues until all items in the sequence are processed.

### **Syntax of For Loop**
```python
for variable in sequence:
    # code to execute
```

- **`variable`**: A temporary variable that takes the value of each item in the sequence one by one.
- **`sequence`**: Any iterable object like a list, tuple, string, or range.

### **Examples of For Loop**

#### Example 1: Iterating through a list
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

#### Example 2: Using a `for` loop with `range()`
The `range()` function generates a sequence of numbers, commonly used in loops for counting or iterating a fixed number of times.
```python
for i in range(5):  # Range generates numbers from 0 to 4
    print(i)
```
Output:
```
0
1
2
3
4
```

#### Example 3: Iterating through a string
```python
name = "Pawan"
for char in name:
    print(char)
```
Output:
```
P
a
w
a
n
```

#### Example 4: Using `else` with a `for` loop
The `else` block in a `for` loop is executed when the loop completes normally (without being interrupted by a `break` statement).
```python
for i in range(5):
    print(i)
else:
    print("Loop Completed")
```
Output:
```
0
1
2
3
4
Loop Completed
```

#### Example 5: Using `break` and `continue` in a `for` loop
- `break` terminates the loop entirely when a condition is met.
- `continue` skips the current iteration and moves to the next iteration.
```python
for num in range(5):
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)

for num in range(5):
    if num == 3:
        continue  # Skip this iteration when num is 3
    print(num)
```

---

## **2. While Loop**

The `while` loop runs as long as the condition specified evaluates to `True`. The condition is checked before each iteration, and if the condition is `True`, the block of code inside the loop is executed. The loop continues until the condition becomes `False`.

### **Syntax of While Loop**
```python
while condition:
    # code to execute
```

- **`condition`**: An expression that evaluates to `True` or `False`. The loop will continue executing as long as the condition remains `True`.

### **Examples of While Loop**

#### Example 1: Simple While Loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count
```
Output:
```
1
2
3
4
5
```

#### Example 2: Using `else` with a While Loop
The `else` block in a `while` loop executes when the loop terminates without encountering a `break` statement.
```python
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("Loop Completed")
```
Output:
```
1
2
3
4
5
Loop Completed
```

#### Example 3: Using `break` and `continue` in a While Loop
- `break` immediately stops the loop when a condition is met.
- `continue` skips the current iteration and moves to the next iteration.
```python
count = 1
while count <= 5:
    if count == 3:
        break  # Stop the loop when count is 3
    print(count)
    count += 1

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the current iteration when count is 3
    print(count)
```

#### Example 4: Countdown Timer (Using `time.sleep()`)
```python
import time

countdown = 5
while countdown > 0:
    print("Time left:", countdown)
    time.sleep(1)  # Pause for 1 second
    countdown -= 1
print("Time's up!")
```
Output (with a 1-second delay between prints):
```
Time left: 5
Time left: 4
Time left: 3
Time left: 2
Time left: 1
Time's up!
```

---

## **Comparison: For Loop vs While Loop**

| Feature               | For Loop                                        | While Loop                                      |
|-----------------------|-------------------------------------------------|-------------------------------------------------|
| **When to use**        | When the number of iterations is known or based on a sequence. | When the number of iterations is unknown and depends on a condition. |
| **Syntax**             | `for var in sequence:`                         | `while condition:`                              |
| **Typical Use Case**   | Iterating over a range, list, tuple, or string. | Repeating until a condition changes (e.g., reading input, waiting for an event). |
| **Termination**        | Loops until all items in the sequence are processed. | Loops until the condition becomes `False`. |
| **Examples**           | Iterating over a list or range.                | Repeating tasks until a specific condition is met (e.g., countdown). |

---

## **Advanced Loop Concepts**

### **Nested Loops**
You can have loops inside other loops, known as **nested loops**.

#### Example of Nested For Loop:
```python
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")
```
Output:
```
i: 0, j: 0
i: 0, j: 1
i: 0, j: 2
i: 1, j: 0
i: 1, j: 1
i: 1, j: 2
i: 2, j: 0
i: 2, j: 1
i: 2, j: 2
```

### **Iterating Over Dictionaries**
You can loop through dictionaries by iterating over keys, values, or both.
```python
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(key, value)
```
Output:
```
a 1
b 2
c 3
```

---

## **Note:**

- **For Loops** are ideal for iterating over sequences and performing a task for each element.
- **While Loops** are more suited for situations where you don’t know how many times you need to loop, but the loop continues based on a condition.
- **Nested Loops** can be used for more complex tasks, such as working with multi-dimensional data.

### **Practices**
- Use `for` loops when the number of iterations is known beforehand.
- Use `while` loops for situations where the loop continues based on a condition.
- Avoid infinite loops (when the condition never becomes `False`).
- Be careful when using `break` and `continue`, as they can disrupt the natural flow of a loop.

---

