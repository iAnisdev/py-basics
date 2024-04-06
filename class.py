class User:
    def __init__ (self , name , age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hello, my name is {self.name}'
    
    def say_age(self):
        return f'I am {self.age} years old'

print(User)
print(type(User))


adam = User('Adam', 25)
print(adam.greeting())
print(adam.say_age())
print(adam.name)
print(adam.age)

eve = User('Eve' ,  28)
print(eve.greeting())
print(eve.say_age())
