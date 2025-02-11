# Identity Operators in Python

x = 5
y = 5  # Small integers (-5 to 256) share the same memory location
print(x is y)  # Output: True

a = [1, 2, 3]
b = [1, 2, 3]  # Different memory locations
print(a is not b)  # Output: True

s1 = "hello"
s2 = "hello"  # Python optimizes memory for short strings
print(s1 is s2)  # Output: True
