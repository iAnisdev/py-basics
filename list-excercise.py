numbersWithDuplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(set(numbersWithDuplicates)))

numbersWithoutDuplicates = []

for number in numbersWithDuplicates:
    if number not in numbersWithoutDuplicates:
        numbersWithoutDuplicates.append(number)

print(numbersWithoutDuplicates)
