from abc import ABC , abstractmethod

class vehicle(ABC):
    
    @abstractmethod
    def go():
        pass

class car(vehicle):
        def go(self):
            print("The car is moving")

class bike(vehicle):
        def go(self):
            print("The bike is moving")


c = car()
c.go()
b = bike()
b.go()

# will throw error
v = vehicle()
v.go()