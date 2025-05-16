"""
The super() keyword in Python is used to REFER to the PARENT class. It is especially useful when a class inherits from multiple parent classes
, and you want to call a method from one of the parent classes. It is used to call parent methods from a child class.
"""
class Parentclass:
    def parent_method(self):
        print("This is parent method")

class Childclass(Parentclass):
    def child_method(self):
        print("This is child method")

        super().parent_method() # calling parent_method inside child_method by using super

a=Childclass()
a.child_method()

print("\n----------------------------------------------------------\n")

class Parent:
    def parent_method(self):
        print("This is parent method")

class Child(Parent):
    def child_method(self):
        print("This is child method")

        super().parent_method()
        # Only parent_method() will not work even though it is inherited from its parent

    def parent_method(self):
        print("This is child class's parent method")

b=Child()
b.child_method()
b.parent_method()

print("\n----------------------------------------------------------\n")

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,ename,eid,lang):

        super().__init__(ename, eid)
        self.lang=lang

Amogh=Programmer("Amogh",12,"SQL")
print(Amogh.name)
print(Amogh.id)
print(Amogh.lang)

print("\n----------------------------------------------------------\n")

# Method overriding

class Parent:
    def greet(self):
        print("Hello from parent")

class Child(Parent):
    def greet(self):    #method overriding
        super().greet()     #call the parent method
        print("Hello from child")

a=Child()
a.greet()