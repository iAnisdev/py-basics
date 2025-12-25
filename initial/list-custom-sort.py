fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

def custom_sort(fruit):
    return len(fruit)

fruits.sort()
print(fruits)

fruits.sort(key=custom_sort)
print(fruits)

fruits.sort(key=custom_sort, reverse=True)
print(fruits)

fruits.sort(key=lambda fruit: fruit.count('e'))

print(fruits)

fruits.sort(key=lambda fruit: fruit.count('a'), reverse=True)

print(fruits)