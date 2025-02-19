### **📜 Notes: Python Set Methods**  

---

## **📌 What is a Set in Python?**  
A **set** is an **unordered**, **mutable**, and **unique collection** of elements. It does not allow **duplicate values** and does not support **indexing** or **slicing**.

```python
# Creating a Set
my_set = {10, 20, 30, 40, 50}
print(my_set)  # Output: {10, 20, 30, 40, 50}

# Duplicates are removed automatically
my_set = {10, 20, 30, 10, 20}
print(my_set)  # Output: {10, 20, 30}
```

---

## **📌 Important Set Methods**

### **1️⃣ Adding Elements**
```python
s = {1, 2, 3}
s.add(4)  # Adds a single element
print(s)  # Output: {1, 2, 3, 4}
```

- **`add(element)`** → Adds a single element to the set.
- ❌ **Cannot add multiple elements at once** using `add()`.

---

### **2️⃣ Updating Sets**
```python
s.update([5, 6, 7])  # Adds multiple elements
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7}
```
- **`update(iterable)`** → Adds multiple elements from an iterable (list, tuple, set).

---

### **3️⃣ Removing Elements**
```python
s.remove(3)  # Removes 3 (gives an error if element not found)
print(s)

s.discard(10)  # Removes 10 if present, otherwise does nothing
print(s)

x = s.pop()  # Removes and returns a random element
print(f"Removed: {x}, Remaining Set: {s}")

s.clear()  # Removes all elements, making it an empty set
print(s)  # Output: set()
```
- **`remove(value)`** → Removes an element; **raises error if not found**.
- **`discard(value)`** → Removes an element; **does NOT raise error if not found**.
- **`pop()`** → Removes **a random element** from the set.
- **`clear()`** → Removes **all elements** from the set.

---

### **4️⃣ Set Operations**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))         # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # {3, 4}
print(A.difference(B))    # {1, 2}
print(B.difference(A))    # {5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```
- **`union(setB)`** → Combines two sets (`A | B`).
- **`intersection(setB)`** → Common elements (`A & B`).
- **`difference(setB)`** → Elements in `A` but not in `B` (`A - B`).
- **`symmetric_difference(setB)`** → Elements in `A` or `B` but **not both** (`A ^ B`).

---

### **5️⃣ Checking Set Relations**
```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))  # True
print(B.issuperset(A))  # True
print(A.isdisjoint(B))  # False (because they have common elements)
```
- **`issubset(setB)`** → Returns `True` if `A` is a subset of `B`.
- **`issuperset(setB)`** → Returns `True` if `A` is a superset of `B`.
- **`isdisjoint(setB)`** → Returns `True` if `A` and `B` have **no common elements**.

---

### **6️⃣ Copying a Set**
```python
original_set = {1, 2, 3}
copy_set = original_set.copy()

print(copy_set)  # Output: {1, 2, 3}
```
- **`copy()`** → Creates a shallow copy of the set.

---

## **📌Set Methods**
| Method | Description |
|--------|-------------|
| `add(element)` | Adds a single element to the set |
| `update(iterable)` | Adds multiple elements to the set |
| `remove(element)` | Removes an element (raises error if not found) |
| `discard(element)` | Removes an element (does NOT raise error) |
| `pop()` | Removes and returns a random element |
| `clear()` | Removes all elements from the set |
| `union(setB)` | Returns a new set with elements from both sets |
| `intersection(setB)` | Returns a set with common elements |
| `difference(setB)` | Returns elements present in one set but not the other |
| `symmetric_difference(setB)` | Returns elements present in either set but not both |
| `issubset(setB)` | Checks if set is a subset of another |
| `issuperset(setB)` | Checks if set is a superset of another |
| `isdisjoint(setB)` | Checks if two sets have no common elements |
| `copy()` | Returns a shallow copy of the set |

---

### **📌 Key Takeaways**
✔ **Sets store only unique values (no duplicates).**  
✔ **Sets are unordered, so indexing is not allowed.**  
✔ **Use `remove()` when you're sure the element exists, otherwise use `discard()`.**  
✔ **Use `update()` for adding multiple elements at once.**  
✔ **Use set operations (`union`, `intersection`, `difference`) for mathematical operations.**  

---
