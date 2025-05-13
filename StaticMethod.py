"""
Static methods in Python are methods/functions that belong to a class without requiring an instance. They are defined using the @staticmethod decorator they don't use self
They have no access to class or instance data i.e. they cant use the instance and class variables directly
"""

class Math:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addtonum(self, n):
        return self.num1 + n

    @staticmethod
    def statadd(a, b):  # no need to use self
        return a + b



statresult = Math.statadd(1, 2)     #class.staticmethod()
print(statresult) # Output: 3

result=Math(5,6)
print(result.addtonum(10))

# result = Math.add(1, 2)   This will not work as this is not a static method

print("--------------------------------------")

# Static methods cannot directly use instance variables (self.variable_name), but you can pass the instance as an argument to the static method if needed.

class Example:
    def __init__(self, value):
        self.value = value  # Instance variable

    @staticmethod
    def show_instance_variable(obj):  # Accept instance as an argument
        return obj.value

# Usage
e = Example(10)
print(Example.show_instance_variable(e))  # Output: 10
