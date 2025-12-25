
def fibonacci(n):
   if n <= 1:
        return n
   else:
        return fibonacci(n-2) + fibonacci(n-1)
    
print(fibonacci(10))
print(fibonacci(0))
print(fibonacci(-1))
print(fibonacci(1))
print(fibonacci(2))


rounds = int(input("Enter the number of rounds: "))

n1 = 0
n2 = 1
next = 0

for i in range(1, rounds+1):
    print(n1)
    next = n1 + n2
    n1 = n2
    n2 = next

    