class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} is {self.age} years old"
        
        
alice =  Person('Alice' , 20)
# print(alice)

country_capitals = dict({
  'England': 'London',
  'Canada': 'Ottawa', 
  'Germany': 'Berlin'
})

print(country_capitals)

capitals = country_capitals.copy()


print(capitals)

country_capitals["Ireland"] = "Dublin"
print(country_capitals)
print(capitals)



print(capitals is country_capitals)

access keys in reversed order
and convert it to a tuple
country = list(reversed(country_capitals.values()))
print(country)


nums = [2 , 7 , 5, 6,4  , 1 , 8 ,3]
print(nums)

print(sorted(nums))
print(sorted(nums , reverse=True))

print(min(nums))
print(max(nums))
print(sum(nums))

print(locals())
print(vars())
print(vars(alice))

ids = [1 , 2 , 3 , 4, 5 , 6 ]

alphabets = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']


for i in zip(ids , alphabets , strict= True):
    print(i)


def cheeseshop(kind,/ ,*arguments,*, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
          "It's really very, VERY runny, sir.",
          shopkeeper="Michael Palin",
          client="John Cleese",
          sketch="Cheese Shop Sketch")




args = [2 , 10, 2]

lst = list(range(*args))

print(lst)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

def test():
    pass



print(test.__doc__)


def sum(a: int , b: int) -> int:
    print(sum.__annotations__)
    return a + b
    
print(sum(3 , 8))
    
lst = [1 , 3, 14 ,8, 4, 2, 24,12, 22]

print(lst)

lst.insert(1 , 2)
print(lst)

last = lst.pop()

print(last)
print(lst)

random = lst.pop(2)

print(random)
print(lst)

random_few = lst.pop(5)
print(random_few)
print(lst)


lst = [{"name": "A", "age": "25"}, {"name": "B", "age": 20}]
lst.sort( key="name")
print(lst)


print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
