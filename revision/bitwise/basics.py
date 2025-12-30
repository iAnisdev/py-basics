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

#Shift Operators -> used to shift bits to left or right in a binary number using << and >>

# left shift (shifts bits to the left, adding 0s on the right)
LEFT_SHIFT_RESULT = FIVE << 1 # shifts 0101 to 1010
print(f"Left Shift Result: {LEFT_SHIFT_RESULT}")  # Output: 10

# right shift (shifts bits to the right, discarding bits on the right)
RIGHT_SHIFT_RESULT = SIX >> 1 # shifts 0110 to 0011
print(f"Right Shift Result: {RIGHT_SHIFT_RESULT}")  # Output: 3
