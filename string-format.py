name = input("Enter your name: ")
age = int(input("Enter your age: "))

# message = "Hello %s, you are %d years old." % (name, age)
# print(message)

message = "Hello {}, you are {} years old.".format(name, age)
print(message)

message = f"Hello {name.upper()}, you are {age} years old."
print(message)

city = "Bangkok"
print(dir(city))
print(help(str))