def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(3)


def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(8))
print(factorial(12))
print(factorial(33))