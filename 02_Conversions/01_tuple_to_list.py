# Convert Tuple to List, Modify it, and Convert Back

t = (5, 2, 9)  # Tuple (immutable)
temp_list = list(t)  # Convert to List
temp_list[1] = 7  # Modify List
t = tuple(temp_list)  # Convert Back to Tuple
print(t)  # Output: (5, 7, 9)
