def greet(name):
    return "Hello, " + name + "!"


print(greet("World"))
print(greet("Alice"))
print(greet("Bob"))


def greetF(name):
    return (f"Hello, {name}!")


print(greetF("World"))

def add(a, b):
    return a + b

print(add(1, 2))
print(add(3, 4))


def isPrime(number):
    if(number < 2):
        return False
    elif(number == 2):
        return True
    else:
        for i in range(2, number):
            if(number % i == 0):
                return False
        return True
    

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(5))
print(isPrime(7))
print(isPrime(11))
print(isPrime(13))
print(isPrime(17))
print(isPrime(19))


def greeting(name, message="Hello"):
    return f"{message}, {name}!"


print(greeting("Alice"))
print(greeting("Alice", "Hi"))

def student_info(*agrs , **kwargs):
    print("agrs" , agrs)
    print("kwargs" , kwargs)
    return "Done"


print(student_info("Math", "Art", name="John", age=22))

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}
print(student_info(*courses, **info))