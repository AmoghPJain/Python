"""
the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the
object's attributes, allowing the object to be fully functional and ready to use.

However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor.
This is where class methods can be used as alternative constructors.
"""

class Employee:

    def __init__(self,name, salary):
        self.name=name
        self.salary=salary
        print(f"Salary of {self.name} is {self.salary}")

    @classmethod    # Additional constructor
    def fromstr(cls,string,sep):
        return Employee(string.split(sep)[0], string.split(sep)[1])

# there are 3 ways to invoke the above Employee class

e1=Employee("Amogh",98000)

string="Harish-90000"
e2=Employee(string.split("-")[0], string.split("-")[1])

# or
e3=Employee.fromstr("Vaishali:99000",":") # calling from class constructor