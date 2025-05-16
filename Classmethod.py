"""
A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole,
rather than on a specific instance of the class. It's decorated with "@classmethod" , followed by a function definition.
The first parameter it receives is cls, which represents the class itself.
"""

class Employee:
    company="Societe Generale"  # class variable

    def showcompany(self):
        print(f"\n{self.name} works in {self.company}")

    @classmethod
    def changecompany(cls,cname):       # when you use @classmethod, by default the first argument wil be taken as class
        cls.company=cname

e1=Employee()
e1.name="Amogh"
e1.showcompany()
print("Employee.company =",Employee.company)     # accessing class variable
print("e1.company =",e1.company)       # accessing instance variable
print("\nAfter changing the company,")
e1.changecompany("Dassault")        # here we are changing the class variable data
e1.showcompany()
print("Employee.company =",Employee.company)

print("\n---------------------------------------------------------------\n")

class Employee:
    total_employees = 0  # Class variable shared across all instances. This value can be changed after calling this

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.total_employees += 1  # Updating class variable

    @classmethod
    def get_total_employees(cls):  # Class method to access the class variable
        return f"Total employees: {cls.total_employees}"

# Creating instances
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")

# Accessing class method
print(Employee.get_total_employees())  # Output: Total employees: 2
print(Employee.total_employees)

print("\n----------------------------------------------\n")

"""In the below example, we create an object by using instance of the class"""
class Circle:
    def __init__(self,radius):
        self.radius=radius

    @classmethod
    def diameter(cls,dia):  # Creates a new instance using the diameter method
        radius=dia/2
        return cls(radius)  # returns with Circle(radius)

c1=Circle(15)
print(c1.radius)
c1.diameter(40)
print(c1.radius)    # This returns 15 instead of 20 as above line is trying to create a new instance over existing. existing instance will have the first preference

c2=Circle.diameter(20) # Creating an instance using the diameter
print(c2.radius)