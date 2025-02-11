## **Operators in Python**
Operators in Python are symbols that perform operations on variables and values. Python has several types of operators:

---

### **1. Arithmetic Operators**
Used for mathematical calculations.

| Operator | Description  | Example (`a = 10, b = 5`) | Output |
|----------|-------------|-----------------|--------|
| `+`  | Addition | `a + b` | `15` |
| `-`  | Subtraction | `a - b` | `5` |
| `*`  | Multiplication | `a * b` | `50` |
| `/`  | Division | `a / b` | `2.0` |
| `//` | Floor Division | `a // b` | `2` |
| `%`  | Modulus (Remainder) | `a % b` | `0` |
| `**` | Exponentiation | `a ** b` | `100000` |

---

### **2. Comparison Operators**
Used to compare values (Returns `True` or `False`).

| Operator | Description | Example (`a = 10, b = 5`) | Output |
|----------|-------------|-----------------|--------|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>`  | Greater than | `a > b` | `True` |
| `<`  | Less than | `a < b` | `False` |
| `>=` | Greater than or equal to | `a >= b` | `True` |
| `<=` | Less than or equal to | `a <= b` | `False` |

---

### **3. Logical Operators**
Used to combine conditional statements.

| Operator | Description | Example (`x = True, y = False`) | Output |
|----------|-------------|---------------------|--------|
| `and` | Returns `True` if both conditions are true | `x and y` | `False` |
| `or`  | Returns `True` if at least one condition is true | `x or y` | `True` |
| `not` | Reverses the condition | `not x` | `False` |

---

### **4. Bitwise Operators**
Used for operations at the bit level.

| Operator | Description | Example (`a = 5 (0101)`, `b = 3 (0011)`) | Output |
|----------|-------------|--------------------|--------|
| `&`  | Bitwise AND | `a & b` | `1` (`0001`) |
| `|`  | Bitwise OR | `a | b` | `7` (`0111`) |
| `^`  | Bitwise XOR | `a ^ b` | `6` (`0110`) |
| `~`  | Bitwise NOT | `~a` | `-6` |
| `<<` | Left shift | `a << 1` | `10` (`1010`) |
| `>>` | Right shift | `a >> 1` | `2` (`0010`) |

---

### **5. Assignment Operators**
Used to assign values to variables.

| Operator | Description | Example (`a = 10`) | Equivalent to |
|----------|-------------|-----------------|--------------|
| `=`  | Assign | `a = 10` | `a = 10` |
| `+=` | Add and assign | `a += 5` | `a = a + 5` |
| `-=` | Subtract and assign | `a -= 5` | `a = a - 5` |
| `*=` | Multiply and assign | `a *= 5` | `a = a * 5` |
| `/=` | Divide and assign | `a /= 5` | `a = a / 5` |
| `//=` | Floor divide and assign | `a //= 5` | `a = a // 5` |
| `%=` | Modulus and assign | `a %= 5` | `a = a % 5` |
| `**=` | Exponent and assign | `a **= 5` | `a = a ** 5` |

---

### **6. Identity Operators**
Used to compare memory locations of two objects.

| Operator | Description | Example (`x = 5, y = 5, z = [1,2]`) | Output |
|----------|-------------|------------------|--------|
| `is` | Returns `True` if both objects have the same memory address | `x is y` | `True` |
| `is not` | Returns `True` if objects have different memory addresses | `x is not z` | `True` |

---

### **7. Membership Operators**
Used to check if a value exists in a sequence (like a list, tuple, or string).

| Operator | Description | Example (`lst = [1,2,3]`) | Output |
|----------|-------------|----------------|--------|
| `in` | Returns `True` if value exists in sequence | `2 in lst` | `True` |
| `not in` | Returns `True` if value does not exist in sequence | `4 not in lst` | `True` |

---

### **Example Program Using Operators**
```python
a = 10
b = 5

# Arithmetic Operators
print(a + b)  # Output: 15

# Comparison Operators
print(a > b)  # Output: True

# Logical Operators
print(a > 5 and b < 10)  # Output: True

# Bitwise Operators
print(a & b)  # Output: 0

# Assignment Operators
a += b
print(a)  # Output: 15

# Identity Operators
x = [1, 2, 3]
y = x
print(x is y)  # Output: True

# Membership Operators
print(3 in x)  # Output: True
```
