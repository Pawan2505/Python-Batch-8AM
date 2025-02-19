### **Python List and Its Methods**  
A **list** in Python is an **ordered, mutable, and iterable** collection of elements. Lists allow **duplicate values** and support various methods for manipulation.

---

## **📌 Creating a List**
```python
# Empty list
my_list = []

# List with elements
numbers = [10, 20, 30, 40, 50]

# List with different data types
mixed_list = [10, "hello", 3.14, True]
```

---

## **🔥 Common List Methods**
### **1️⃣ Adding Elements to a List**
| Method | Description | Example |
|--------|-------------|---------|
| `append()` | Adds an element at the end | `list.append(100)` |
| `insert()` | Inserts an element at a specific index | `list.insert(2, 99)` |
| `extend()` | Adds multiple elements from another iterable | `list.extend([6, 7, 8])` |

```python
numbers = [1, 2, 3]
numbers.append(4)       # [1, 2, 3, 4]
numbers.insert(1, 100)  # [1, 100, 2, 3, 4]
numbers.extend([5, 6])  # [1, 100, 2, 3, 4, 5, 6]
print(numbers)
```

---

### **2️⃣ Removing Elements from a List**
| Method | Description | Example |
|--------|-------------|---------|
| `remove()` | Removes first occurrence of a value | `list.remove(30)` |
| `pop()` | Removes an element at a specific index (default: last) | `list.pop(2)` |
| `clear()` | Removes all elements from the list | `list.clear()` |

```python
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)  # [10, 20, 40, 50]
numbers.pop(1)      # Removes element at index 1 → [10, 40, 50]
numbers.clear()     # []
print(numbers)
```

---

### **3️⃣ Accessing Elements in a List**
| Method | Description | Example |
|--------|-------------|---------|
| Indexing | Access element by index | `list[2]` |
| Negative Indexing | Access from end | `list[-1]` |
| Slicing | Get a sublist | `list[1:4]` |

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[2])     # 30
print(numbers[-1])    # 50
print(numbers[1:4])   # [20, 30, 40]
```

---

### **4️⃣ Finding Elements in a List**
| Method | Description | Example |
|--------|-------------|---------|
| `index()` | Returns the index of the first occurrence of an element | `list.index(30)` |
| `count()` | Counts the occurrences of a value | `list.count(20)` |

```python
numbers = [10, 20, 30, 20, 40]
print(numbers.index(30))  # 2
print(numbers.count(20))  # 2
```

---

### **5️⃣ Sorting and Reversing a List**
| Method | Description | Example |
|--------|-------------|---------|
| `sort()` | Sorts list in ascending order | `list.sort()` |
| `sort(reverse=True)` | Sorts list in descending order | `list.sort(reverse=True)` |
| `reverse()` | Reverses the list | `list.reverse()` |

```python
numbers = [50, 20, 40, 10, 30]
numbers.sort()  # [10, 20, 30, 40, 50]
numbers.sort(reverse=True)  # [50, 40, 30, 20, 10]
numbers.reverse()  # [10, 30, 40, 20, 50]
print(numbers)
```

---

### **6️⃣ Copying a List**
| Method | Description | Example |
|--------|-------------|---------|
| `copy()` | Returns a shallow copy of the list | `new_list = list.copy()` |

```python
numbers = [1, 2, 3]
copy_numbers = numbers.copy()
print(copy_numbers)  # [1, 2, 3]
```

---

### **7️⃣ Joining and Splitting Lists**
| Method | Description | Example |
|--------|-------------|---------|
| `+` Operator | Joins two lists | `list1 + list2` |
| `join()` | Joins elements into a string | `' '.join(list)` |

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
print(combined)
```

```python
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"
print(sentence)
```

---

### **8️⃣ List Comprehension (Advanced)**
| Method | Description | Example |
|--------|-------------|---------|
| List Comprehension | Create a list using a single line | `[x for x in list]` |

```python
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]  # [1, 4, 9, 16, 25]
print(squared)
```

---

### **🔥 Summary of List Methods**
| Method | Purpose |
|--------|---------|
| `append(x)` | Adds `x` to the end of the list |
| `insert(i, x)` | Inserts `x` at index `i` |
| `extend(iterable)` | Appends all elements from an iterable |
| `remove(x)` | Removes the first occurrence of `x` |
| `pop(i)` | Removes element at index `i` (default: last) |
| `clear()` | Removes all elements |
| `index(x)` | Returns the index of `x` |
| `count(x)` | Returns the count of `x` |
| `sort()` | Sorts the list in ascending order |
| `reverse()` | Reverses the list |
| `copy()` | Returns a shallow copy |
| `join()` | Joins elements into a string |
