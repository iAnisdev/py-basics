number_set = {1, 2, 3, 4, 5}
print(number_set)
print(1 in number_set)
print(6 in number_set)
number_set.add(6)
print(number_set)
number_set.add(1)
print(number_set)
number_set.remove(6)
print(number_set)
number_set.discard(5)
print(number_set)

numbers_dup_set = {  3, 4, 5 , 1, 2, 3, 4, 5, 1, 2}
print(numbers_dup_set)

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
