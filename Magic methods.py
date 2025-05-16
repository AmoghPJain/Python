class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return (f"The name of the employee is {self.name}")

    def __repr__(self):
        return (f"The name of the employee is {self.name}")

e1 = Employee("Amogh")
print(len(e1))  # This will not work if __len__ method is not defined
print(str(e1))  # This will not work if __str__ method is not defined
print(repr(e1))  # This will not work if __repr__ method is not defined. Mainly used by developers for debugging

print("\n-----------------------------------------\n")

class Example:
    def __repr__(self):
        return "Example()--"

obj = Example()
print(repr(obj))  # Output: Example()

