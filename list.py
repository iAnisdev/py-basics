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