### **Frozen Set in Python**
A **frozenset** is an **immutable** version of a set in Python. It is similar to a set, but once created, **its elements cannot be modified (added or removed)**.

#### **Syntax:**
```python
fs = frozenset([1, 2, 3, 4, 5])
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})
```

---

## **Characteristics of Frozen Sets:**
- **Immutable** – Cannot be modified after creation.
- **Unordered** – Elements are not stored in a specific order.
- **Duplicates Not Allowed** – Like sets, frozensets do not allow duplicate values.
- **Hashable** – Since they are immutable, frozensets can be used as dictionary keys.

---

## **Frozen Set Methods**
Even though frozensets are immutable, they support several operations similar to sets.

### **1. `copy()`**
Returns a shallow copy of the frozenset.
```python
fs = frozenset([1, 2, 3])
new_fs = fs.copy()
print(new_fs)  # Output: frozenset({1, 2, 3})
```

### **2. `union()`**
Returns a new frozenset containing elements from both sets.
```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
result = fs1.union(fs2)
print(result)  # Output: frozenset({1, 2, 3, 4, 5})
```

### **3. `intersection()`**
Returns a new frozenset containing elements that are present in both sets.
```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
result = fs1.intersection(fs2)
print(result)  # Output: frozenset({3, 4})
```

### **4. `difference()`**
Returns a new frozenset with elements from the first set that are not in the second set.
```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
result = fs1.difference(fs2)
print(result)  # Output: frozenset({1, 2})
```

### **5. `symmetric_difference()`**
Returns a new frozenset containing elements that are in either of the sets, but not in both.
```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
result = fs1.symmetric_difference(fs2)
print(result)  # Output: frozenset({1, 2, 5, 6})
```

### **6. `issubset()`**
Checks if all elements of the frozenset are present in another set.
```python
fs1 = frozenset([1, 2])
fs2 = frozenset([1, 2, 3, 4])
print(fs1.issubset(fs2))  # Output: True
```

### **7. `issuperset()`**
Checks if the frozenset contains all elements of another set.
```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([1, 2])
print(fs1.issuperset(fs2))  # Output: True
```

### **8. `isdisjoint()`**
Returns `True` if the sets have no common elements.
```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
print(fs1.isdisjoint(fs2))  # Output: True
```

---

## **Key Differences: Set vs Frozen Set**
| Feature      | Set (`set()`) | Frozen Set (`frozenset()`) |
|-------------|--------------|----------------|
| **Mutable** | ✅ Yes  | ❌ No (Immutable) |
| **Allows Duplicate Elements** | ❌ No | ❌ No |
| **Unordered** | ✅ Yes  | ✅ Yes |
| **Supports Add/Remove** | ✅ Yes | ❌ No |
| **Hashable (Can be used as dict keys)** | ❌ No | ✅ Yes |

---

## **When to Use Frozen Sets?**
- When you need a **read-only set** that cannot be modified.
- When you need to **use a set as a dictionary key**.
- When you need to store **immutable collections** inside other sets.
