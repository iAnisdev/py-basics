pi = 3.14159

print("Pi is approximately {:.2f}".format(pi))


price = 1000000000
print("The price is ${:,}".format(price))
print("The price is ${:,.2f}".format(price))
# Binary
print("The price is ${:b}".format(price))
# Octal
print("The price is ${:o}".format(price))
# Hexadecimal
print("The price is ${:x}".format(price))
print("The price is ${:X}".format(price))
# Exponential notation
print("The price is ${:e}".format(price))
print("The price is ${:E}".format(price))
# Percentage
print("The price is {:.2%}".format(price))
# Padding
print("The price is {:10}".format(price))
print("The price is {:010}".format(price))
