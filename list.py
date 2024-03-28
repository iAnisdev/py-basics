users = ["A" , "B" , "C" , "D" , "E"]
print(users)
print(users[0])
print(users[:3])
print(users[2:])
print(users[2:4])
users.append("F")
print(users)
users.insert(0 , "-A")
print(users)
users.remove("D")
print(users)
print("A" in users)
print("D" in users)
print(len(users))
users.extend(["G" , "H"])
print(users)
users.pop()
print(users)
users.reverse()
print(users)
users.sort()
print(users)
users.sort(reverse=True)
print(users)

numbers = [7 , 5 , 3 , 8 , 2 , 9 , 1 , 4 , 6]
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
reverse_sorted_numbers = sorted(numbers , reverse=True)
print(reverse_sorted_numbers)
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(numbers.index(8))
print(numbers.count(5))
print(10 in numbers)
print(5 in numbers)

for i in numbers:
    print(i)

for(i , user) in enumerate(users ):
    print(i , user)
    
print('-'.join(users))