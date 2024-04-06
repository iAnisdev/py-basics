class User:
    isAdmin = False
    isActive = True
    def __init__ (self , name , age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hello, my name is {self.name}'
    
    def say_age(self):
        return f'I am {self.age} years old'
    
    def __str__ (self):
        return "User is {} and {} years old".format(self.name, self.age)

print(User)
print(type(User))


adam = User('Adam', 25)
print(adam)
print(adam.greeting())
print(adam.say_age())
print(adam.name)
print(adam.age)

eve = User('Eve' ,  28)
print(eve.greeting())
print(eve.say_age())

print(adam.isAdmin)
print(eve.isAdmin)
eve.isAdmin = True
print(eve.isAdmin)

print(User.isActive)
print(adam.isActive)
print(eve.isActive)

User.isActive = False
print(User.isActive)
print(adam.isActive)
print(eve.isActive)

class Editor (User):
    pass
class Admin (User):
    isAdmin = True
    say_age = lambda self: 'I am an Admin and i never age'

james = Editor('James', 30)
print(james.greeting())
print(james.say_age())
print(james.isAdmin)

john = Admin('John', 35)
print(john.greeting())
print(john.say_age())
print(john.isAdmin)

print(isinstance(john, Admin))
print(isinstance(john, User))
print(isinstance(john, Editor))
print(Admin.__bases__)