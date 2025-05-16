"""
Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.
This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes
"""

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):     # This is returned whenever a class is being called
        return (f"Vector({self.x}, {self.y})")

v1=Vector(1,8)
v2=Vector(3,12)

result=v1+v2
print(result)
print(result.x)

print("\n-----------------------------\n")

class Vector1:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y   # here we are not returning as Vector class

    def __repr__(self):
        return (f"Vector({self.x}, {self.y})")

v3=Vector(1,8)
v4=Vector(3,12)

result=v3+v4
print(result)
print(result.x)     # this will not work as in add we are not returning it as Vector class

print("\n-----------------------------\n")

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __lt__(self, other):  # Overload '<' operator
        return self.pages < other.pages

# Usage
book1 = Book("Book A", 150)
book2 = Book("Book B", 300)
print(book1 < book2)  # Output: True (because 150 < 300)
print(book2 < book1)  # Output: True (because 150 < 300)
