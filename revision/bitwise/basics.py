FIVE = 5 #0101
SIX = 6 #0110

# and (True if both bits are 1)

AND_RESULT = FIVE & SIX  
print(f"AND Result: {AND_RESULT}")  # Output: 4 0100

# or (True if at least one bit is 1)

OR_RESULT = FIVE | SIX  
print(f"OR Result: {OR_RESULT}")  # Output: 7 0111

# xor (True if only one bit is 1, false if both are 0 or both are 1)

XOR_RESULT = FIVE ^ SIX  
print(f"XOR Result: {XOR_RESULT}")  # Output: 3 0011

# not (inverts the bits)
NOT_FIVE_RESULT = ~FIVE  
print(f"NOT FIVE Result: {NOT_FIVE_RESULT}")  # Output: -6 (it is 6 because of two's complement representation)

# two 's complement representation
# it will be negative because the leftmost bit (sign bit) is 1 and in binary representation, 1 indicates a negative number and 0 indicates a positive number.
# to get the positive value back, we can do the following:
POSITIVE_VALUE = ~NOT_FIVE_RESULT 
print(f"Positive Value from NOT Result: {POSITIVE_VALUE}")  # Output: 5