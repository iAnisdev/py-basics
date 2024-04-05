numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10 , 11, 12 , 13, 14, 15]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)


odds = [number for number in numbers if number % 2 != 0]

print(odds)