class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showdetails(self):
        print(f"\nThe age of employee named {self.name} is {self.age}")

class Programmer(Employee): # Inherited class
    def showlanguage(self):
        print("Default language used is Python")

b=Programmer("Amogh",28)
b.showdetails()
b.showlanguage()

print("\nAccess specifiers:")

"""
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class 
while implementing the concepts of inheritance.

Public access modifier - by default
Protected access modifier (_)
Private access modifier (__)
"""

"""
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword 
ie. self.var_name are public accessed.
"""

print("\nPublic Access specifiers-----------------------\n")

class student:
    def __init__(self,age,name):
        self.age=age
        self.xyzname=name

a=student(3,"Kanvi")
print(f"Student name = {a.xyzname} and age is {a.age}")


print("\nPrivate access specifiers-----------------------\n")
"""
Private members of a class (variables or methods) are those members which are ONLY ACCESSIBLE INSIDE the CLASS. We cannot use private members outside of class.
There is no strict concept of "private" access modifiers like in other programming languages, however a convention has been established to indicate that a variable or method
should be considered as private by prefixing its name with a double underscore (__).
Code outside the class can still access these "private" variables and methods indirectly(i.e. Name Mangling), but it is generally understood that they should not be accessed/ modified.
"""

class Studentprivate:
    def __init__(self,age,name):
        self.__age=age      # An indication of private variable
        self.xyzname=name

    def __funName(self):
        self.y=34
        print(self.y)

class Subject(Studentprivate):
    pass  # we use pass when defining an empty function or class that you plan to implement later

s1=Studentprivate(21,"Harry")
S2=Subject

"""
Below will give error as we are trying to access private objects

# calling by object of class Student
print(s1.__age)
print(s2.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())
"""

# however they can be accessed indirectly
print(s1._Studentprivate__age)
print(s1._Studentprivate__funName())

print("\nProtected access specifiers-----------------------")
"""
It is intended to be accessed only by the class itself and its subclasses.In Python, the convention for indicating that a member is protected is to prefix its name with a single 
underscore (_).It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. 
"""

class Studentprotected:
    def __init__(self,age,name):
        self._age=age      # An indication of private variable
        self.xyzname=name


object1=Studentprotected(29,"Parth")
print(object1._age)

print("\n-------------------------------------------\n")

        # If there are paremeters defined in parent class but not in child class when you are invoking child class you would have to still pass the parameters

class Employee:
    def __init__(self, name):
        self.name = name  # Instance variable in parent class

    def show(self):
        print("Employee name is", self.name)

class Child(Employee):
    def display_name(self):  # Method in child class
        print(f"Name from Employee class: {self.name}")

# Create an instance of Child
child_instance = Child("Amogh")
child_instance.display_name()  # Output: Name from Employee class: Amogh

print("\nMultiple Inheritance------------------------------------\n")

"""Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. 
This can be useful in situations where a class needs to inherit functionality from multiple sources.
"""

class Dancer:
    def __init__(self,dancetype):
        self.dancetype=dancetype

    def show(self):
        print("Name of dance form is",self.dancetype)

class Danceremployee(Employee, Dancer): # Inheriting 2 classes
    def __init__(self,dancetype,name):
        self.dancetype=dancetype
        self.name=name

    def __str__(self):
        return (f"Employee {self.name} knows {self.dancetype} danceform")

ep1=Danceremployee("Kathak","Amogh")
print(ep1)
ep1.show()     # since both employee and dance class have show() method, Employee's show method will be called since employee is inherited first(line 130). you can try vice versa

print("\nMultilevel Inheritance------------------------------------\n")

"""
Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class.
This type of inheritance allows you to build a hierarchy of classes where one class builds upon another
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

dog=Dog("Tommy","pug")
print(dog.name)
dog.show_details()
print(dog.breed)

print("\nHybrid and Hierarchical Inheritance------------------------------------\n")
# Hybrid inheritance is a combination of multiple inheritance and single inheritance.
# Hierarchical inheritance is a concept where one class serves as a parent (or superclass) for multiple child classes (or subclasses) i.e. Single parent multiple children