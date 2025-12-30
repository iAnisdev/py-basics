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
# In Python, integers are infinite-width signed integers.
# The rule is: ~x = -(x + 1)
NOT_FIVE_RESULT = ~FIVE  
print(f"NOT FIVE Result: {NOT_FIVE_RESULT}")  # Output: -6

# Applying NOT twice returns the original number
POSITIVE_VALUE = ~~FIVE
print(f"Positive Value from double NOT: {POSITIVE_VALUE}")  # Output: 5

#Shift Operators -> used to shift bits to left or right in a binary number using << and >>

# left shift (shifts bits to the left, adding 0s on the right)
LEFT_SHIFT_RESULT = FIVE << 1 # shifts 0101 to 1010
print(f"Left Shift Result: {LEFT_SHIFT_RESULT}")  # Output: 10

# right shift (shifts bits to the right, discarding bits on the right)
RIGHT_SHIFT_RESULT = SIX >> 1 # shifts 0110 to 0011
print(f"Right Shift Result: {RIGHT_SHIFT_RESULT}")  # Output: 3

# Bit Masks
# Bit masks are used to isolate or manipulate specific bits within a binary number.

Five = 0b0101  # Binary representation of 5
Mask_LAST_ONE = 0b0001  # Mask to isolate the last bit
# CHECK if the last bit is set (1) or not (0)
Isolated_Last_Bit = Five & Mask_LAST_ONE
print(f"Isolated Last Bit: {Isolated_Last_Bit}")  # Output: 1

#Check if the second bit is set (1) or not (0)
Mask_SECOND_ONE = 0b0010  # Mask to isolate the second bit
Isolated_Second_Bit = Five & Mask_SECOND_ONE
print(f"Isolated Second Bit: {Isolated_Second_Bit}")  #

# Set the second bit to 1
Set_Second_Bit = Five | Mask_SECOND_ONE
print(f"Set Second Bit Result: {Set_Second_Bit}")  # Output: 7

# Clear the last bit (set it to 0)
Clear_Last_Bit = Five & ~Mask_LAST_ONE
print(f"Clear Last Bit Result: {Clear_Last_Bit}")  # Output: 4

# Toggle the second bit
Toggle_Second_Bit = Five ^ Mask_SECOND_ONE
print(f"Toggle Second Bit Result: {Toggle_Second_Bit}")  # Output: 7
