#!/usr/bin/python3

def validUTF8(data):
    num_bytes = 0

# Checks the first few bits of the byte.
    first_byte = [0b11111111, 0b11111110, 0b11111100, 0b11111000, 0b11110000]
    valid_begin_bits = [
        0b00000000,
        0b11000000,
        0b11100000,
        0b11110000,
        0b11111000
    ]
    continuation_byte = 0b11000000
    continuation_bits = 0b10000000


# Iterate through the data.
    for byte in data:
        if num_bytes == 0:
            # Find out how many bytes are in UTF-8 character.
            for i in range(5):
                if byte & first_byte[i] == valid_begin_bits[i]:
                    num_bytes = i
                    break
# 1-byte character is valid
            if num_bytes == 0:
                continue
        # If num_bytes is is more than 4 or 0, it is invalid.
            if num_bytes == 1 or num_bytes > 4:
                return False
    else:
        # Checks the continuation byte.
        if (byte & continuation_byte) != continuation_bits:
            return False
        # Decrease the number of bytes to process
        num_bytes -= 1
# Everything is valid.
    return num_bytes == 0
