# Collection Data Types in Python

l = [3, 6, 7.9, True, 3, 6]  # List (mutable)
l[1] = 99  

t = (5, 2, 9)  # Tuple (immutable)
# t[0] = 45  # Not allowed (Immutable)

s = {2, 4, 8, 2, 6, 4}  # Set (unique, unordered)
f = frozenset({2, 3, 5, 7, 2, 5})  # Immutable set

d = {'id': 1, 'name': 'Rahul', 'age': 20}  # Dictionary (mutable)
d['age'] = 44  
d.update({'name': "Pawan", 'age': 990})  

print(l, t, s, f, d)
