Rules of UTF-8 encoding:
    * A UTF-8 character can be 1 to 4 bytes long
    * The number of bytes in a UTF-8 character is determined by the leading bits of the first byte.
    * For multi-bytes character (2-4 bytes), each of the subsequent bytes must start with '0xxxxxx'.