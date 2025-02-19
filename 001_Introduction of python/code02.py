# # In Python, sets are mutable, meaning you can add or remove elements from a set. However, sets do not support indexing or item assignment because they are unordered collections.


# # set
# s = {12, 34, 56, 78, 8, 12}

# # s[1] = 122  # ❌ This will cause an error

# print(s)

# # s.add(122,344,555) # not ok

# s.add(122) # ok



# print(s)

# # s.remove(10) # it will give error if data not found

# s.discard(10)  # it will not give error if data not found


# print(s)

# # s.update([8,88])

# s.update([100, 200])

# print(s)

# # convert set to list

# l = list(s)

# print(l)

# l[1] = 111

# print(l)

# st = set(l)

# print(st)


# Empty list
my_list = []

# List with elements
numbers = [10, 20, 30, 40, 50]

print(numbers)
# List with different data types
mixed_list = [10, "hello", 3.14, True]


print(mixed_list)

# List Methods

# 1. Adding Elements to a List

numbers.append(100)
# numbers.append(100,200) # not ok

numbers.extend([200,300,400])

numbers.insert(3,333)
numbers.insert(3,333)
numbers.append(30)

print(numbers)

# 2. Removing Elements from a List

numbers.remove(30) #Removes first occurrence of a value

numbers.pop() #Removes an element at a specific index (default: last)

numbers.pop(0)
print(numbers)

numbers.clear()

print(numbers)

numbers = [10, 20, 30, 40,20, 50]

print(numbers)

print(numbers[2])     # 30
print(numbers[-1])    # 50 Access from end
print(numbers[1:4])   # [20, 30, 40] slicing :Get a sublist

#4. Finding Elements in a List

print(numbers.index(10)) #Returns the index of the first occurrence of an element
print(numbers.count(20)) #Counts the occurrences of a value

# 5. Sorting and Reversing a List
print(numbers)

# numbers.sort()

print(numbers)

# numbers.sort(reverse=True)

print(numbers)

numbers.reverse()

print(numbers)


# 6.Copying a List

numbers = [1, 2, 3]
copy_numbers = numbers.copy()
print(copy_numbers)  # [1, 2, 3]


#7. Joining and Splitting Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
print(combined)
