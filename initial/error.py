# 1. Syntax Error
# print(0/0))
# 2. exception / ZeroDivision Error
# print(0/0)

# 3. Exception Error
# number = 4
# if number > 2:
#     raise Exception("Number is greater than 2.")
# print(number)

# assert (number < 5), "Number is greater than 5."
# print(number)

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    raise Exception("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 