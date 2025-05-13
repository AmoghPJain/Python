"""
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to
store information that is common to all instances of the class.

Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to
store information that is specific to each instance of the class.
"""
class Employee:

    companyname="Societe Generale"  # class variable.

    def __init__(self, name):
        self.name=name
        self.raise_amount=0.02  # instance variable. This value can be changed for diff instances/objects

    def showdetails(self):
        print(f"Name of the employee working in {self.companyname} is {self.name} and raise amount is {self.raise_amount}")

emp1=Employee("Amogh")

emp1.showdetails()  # even if you are not passing any parameters, emp1 default parameter will be passed in place of self
# Employee.showdetails(emp1) # if you are calling as above it will be internally converted as Employee.showdetails(emp1) where emp1 is passed as a parameter

print("---------------------------------------------------")


class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable += 1

    def print_class_variable(self):
        print(MyClass.class_variable)


obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

obj1.print_class_variable()  # Output: 2
obj2.print_class_variable()  # Output: 2
obj3.print_class_variable()  # Output: 2

print("---------------------------------------------------")


class MyClass:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name()  # Output: John
obj2.print_name()  # Output: Jane