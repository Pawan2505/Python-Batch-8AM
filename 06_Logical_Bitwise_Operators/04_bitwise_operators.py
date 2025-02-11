# Bitwise Operators in Python

a = 10  # 1010 in binary
b = 5   # 0101 in binary

print(a & b)  # AND: 0000 -> 0
print(a | b)  # OR:  1111 -> 15
print(a ^ b)  # XOR: 1111 -> 15
print(~a)  # NOT:  -(10+1) -> -11
print(a << 1)  # Left Shift: 10100 -> 20
print(a >> 1)  # Right Shift: 0101 -> 5
