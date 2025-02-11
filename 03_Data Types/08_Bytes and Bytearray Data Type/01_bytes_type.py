# Bytes (Immutable)
byte_data = bytes([65, 66, 67])
print("Bytes:", byte_data, type(byte_data))

# Bytearray (Mutable)
mutable_byte = bytearray([68, 69, 70])
mutable_byte[0] = 72  # Changing first byte
print("Bytearray:", mutable_byte)
