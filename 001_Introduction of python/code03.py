
# tuple

# t = (12,34,56,34, ' ',9,34)

# t[0] = 66

# print(t)
# print(t.count(34))
# print(t.index(34))

# Tuple Operations

# 1. Tuple Concatenation (+)

# tp1 = (1,2,3,4)
# tp2 = (5,6,7,8)

# t = tp1+tp2

# print(t)

# 2. Tuple Repetition (*)

# t = (1,2,3)

# print(t*2)

#  3. Membership Testing (in)

# t = (1,2,3,4)

# print(1 in t)
# print(11 in t)

# 4. Tuple Slicing

# t = (1,2,3,4,5,6,7)

# print(t[1:5])
# print(t[:5])
# print(t[0:5])

# 5. Tuple Unpacking

# t = (1,2,3)

# a,b,c = t

# print(a,b,c)


# Frozen Set in Python
# A frozenset is an immutable version of a set in Python. It is similar to a set, but once created, its elements cannot be modified (added or removed).

# fs = frozenset([1,2,3,4,5])

# # fs.add(23) #not ok

# print(fs)


# 1. copy()

# fs = frozenset([1,2,3,4,5])

# new_fs  = fs.copy()


# print(new_fs)

# 2. union()

# fs1 = frozenset([1,2,3,4,5])
# fs2 = frozenset([4,5,6,7])

# print(fs1.union(fs2))

# 3. intersection()

# fs1 = frozenset([1,2,3,4,5])
# fs2 = frozenset([4,5,6,7])

# print(fs1.intersection(fs2))

# 4. difference()

# fs1 = frozenset([1,2,3,4,5])
# fs2 = frozenset([4,5,6,7])

# print(fs2.difference(fs1))

# 5. symmetric_difference()

# fs1 = frozenset([1,2,3,4,5])
# fs2 = frozenset([4,5,6,7])

# print(fs2.symmetric_difference(fs1))

# 6. issubset()

# fs1 = frozenset([4,5])
# fs2 = frozenset([4,5,6,7])

# print(fs1.issubset(fs2))

# 7. issuperset()

# fs1 = frozenset([1, 2, 3, 4])
# fs2 = frozenset([1, 2])
# print(fs1.issuperset(fs2))  # Output: True


# 8. isdisjoint()

# fs1 = frozenset([1, 2, 3])
# fs2 = frozenset([4, 5, 6])
# print(fs1.isdisjoint(fs2))  # Output: True
