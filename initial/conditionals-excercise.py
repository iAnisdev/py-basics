weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
result = 0
result_unit = ""
if unit == 'L':
    result = weight * 0.45
    result_unit = "Kgs"
else:
    result = weight / 0.45
    result_unit = "Lbs"
print("You are " + str(format(result , '.2f')) + " " + result_unit + ".")