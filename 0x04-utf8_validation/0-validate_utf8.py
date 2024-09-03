#!/usr/bin/python3
"""
This module contains a function to validate if a list of integers represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (List[int]): A list of integers where each integer represents
                      1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    # check if a byte is a valid continuation byte (10xxxxxx)
    continuation_byte = 0b11000000
    continuation_bits = 0b10000000

    for byte in data:
        # If byte is outside the range of valid bytes [0, 255], return False
        if byte < 0 or byte > 255:
            return False

        if num_bytes == 0:
            # Determine how many bytes in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):
                # 1-byte character should start with 0 (0xxxxxxx)
                return False
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte & continuation_byte) != continuation_bits:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, then we are missing continuation bytes
    return num_bytes == 0
