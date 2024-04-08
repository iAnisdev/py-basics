class Employee :
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def display(self):
        print("Name: ", self.name)
        print("Dept: ", self.dept)

class Manager(Employee):
    isManager = True

class Accountant(Employee):
    isAccountant = True

class CFO(Manager, Accountant):
    isCFO = True


e1 = Employee("John", "HR")
e1.display()

m1 = Manager("James", "IT")
m1.display()

a1 = Accountant("Eve", "Finance")
a1.display()

c1 = CFO("Adam", "Finance")
c1.display()
