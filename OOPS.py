"""
A class is a blueprint/template for creating objects. It defines the properties and methods that an object of that class will have.
An object is an instance of a class, and it contains its own data and methods. For example, you could create a class called "Person" that has properties such as name and age and
methods such as speak() and walk().Each instance of the Person class would be a unique object with its own name and age,but they would all have the same methods to speak and walk.
"""

class Person:
    name="Amogh"        # Property
    occupation="Software Engineer"  # Property

    def info(self):     # method
        print(f"{self.name} is a {self.occupation}")

    def __init__(self):         # Always constructors are called first
        print("Welcome..")


a=Person()          # object
a.name="Vaishali"
a.info()


class Person1:
    #Constructor i.e a method which will be invoked each time an object is created
    def __init__(self,name,occ):         # Parameterised constructor
        print(f"{name} is a {occ}")

        """
        self.name and self.occupation are used in the constructor to store the values as variables.
        This way, they can be accessed by other methods in the class. If they are not added, then the parameters cant be accessed by other methods in the class
        
        NOTE: even if you define constructor at the end of a class, it will be called first.
        """

        self.name=name
        self.occupation=occ

    def info(self):
        print(f"\n{self.name} is a {self.occupation}")

a=Person1("Harini","HR")        # 2 parameters must be passed as the constructor is expecting 2 params
b=Person1("Subhray",'developer')

# a.info()
b.info()

class Employee:
    def __init__(self, name):
        self.name=name

    def showdetails(self):
        print(f"Name of the employee is {self.name}")

emp1=Employee("Amogh")