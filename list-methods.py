numbers  = [7 , 5 , 3 , 8 , 2 , 9 , 1 , 4 , 6]
first , second , *rest = numbers
print(first)
print(second)
print(rest)
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
mapped_numbers = map(lambda x: x * 2, sorted_numbers)
print(list(mapped_numbers))

filtered_numbers = filter(lambda x: x % 2 == 0, sorted_numbers)
print(list(filtered_numbers))