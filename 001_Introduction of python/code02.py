# Python List and Set Methods

# ----------------- #
# 📌 Working with Sets
# ----------------- #

# ✅ Creating a set (unordered & unique values)
s = {12, 34, 56, 78, 8, 12}  # Duplicates are removed automatically
print(s)

# ❌ Indexing not allowed
# s[1] = 122  # This will cause an error

# ✅ Adding elements to a set
s.add(122)  # Adds a single element
print(s)

# ❌ s.add(122,344,555)  # This will give an error (add() takes only one argument)

# ✅ Removing elements
# s.remove(10)  # ❌ Will cause an error if element not found
s.discard(10)  # ✅ Will NOT give an error if element is not found
print(s)

# ✅ Updating set with multiple values
s.update([100, 200])  # Adds multiple elements to the set
print(s)

# ✅ Converting Set to List
l = list(s)  # Convert set to list for indexing
print(l)

# ✅ Modifying list elements
l[1] = 111  # Changing second element
print(l)

# ✅ Converting List back to Set
st = set(l)  # Convert list back to set
print(st)


# ----------------- #
# 📌 Working with Lists
# ----------------- #

# ✅ Creating Lists
numbers = [10, 20, 30, 40, 50]  # List with elements
print(numbers)

mixed_list = [10, "hello", 3.14, True]  # List with different data types
print(mixed_list)


# ----------------- #
# ✅ 1. Adding Elements to a List
# ----------------- #
numbers.append(100)  # Adds 100 to the end
numbers.extend([200, 300, 400])  # Adds multiple elements
numbers.insert(3, 333)  # Inserts 333 at index 3
numbers.insert(3, 333)  # Again inserts 333 at index 3
numbers.append(30)  # Adds another 30
print(numbers)


# ----------------- #
# ✅ 2. Removing Elements from a List
# ----------------- #
numbers.remove(30)  # Removes first occurrence of 30
numbers.pop()  # Removes last element
numbers.pop(0)  # Removes first element
print(numbers)

numbers.clear()  # Removes all elements
print(numbers)


# ----------------- #
# ✅ 3. Accessing Elements
# ----------------- #
numbers = [10, 20, 30, 40, 20, 50]
print(numbers)
print(numbers[2])  # Access by index → 30
print(numbers[-1])  # Access from the end → 50
print(numbers[1:4])  # Slicing (sublist) → [20, 30, 40]


# ----------------- #
# ✅ 4. Finding Elements
# ----------------- #
print(numbers.index(10))  # Returns index of first occurrence of 10
print(numbers.count(20))  # Counts occurrences of 20


# ----------------- #
# ✅ 5. Sorting and Reversing a List
# ----------------- #
print(numbers)  # Original list

numbers.sort()  # Sorts in ascending order
print(numbers)

numbers.sort(reverse=True)  # Sorts in descending order
print(numbers)

numbers.reverse()  # Reverses the order of elements
print(numbers)


# ----------------- #
# ✅ 6. Copying a List
# ----------------- #
numbers = [1, 2, 3]
copy_numbers = numbers.copy()  # Creates a copy of the list
print(copy_numbers)


# ----------------- #
# ✅ 7. Joining Lists
# ----------------- #
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # Joins two lists
print(combined)
