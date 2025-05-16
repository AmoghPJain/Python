"""fibonacci series"""
print("\n")

def generate_fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    if n <= 0:
        return []  # Return an empty list for invalid input
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b     # Both values are calculated first, and assignment happens simultaneously.
    return fibonacci_series

print(a:=generate_fibonacci(5))

print("--------------------------------------------")
"""Prime numbers"""
print("\n")

b=[]
for i in range(2,101):
    for x in range(2,50):
        b.append(i*x)

a=[prime for prime in range(1,101) if prime not in b]
a.remove(1)
print(a)


print("--------------------------------------------")
"""Class method"""
print("\n")

class Employee:

    emphike=10

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def employeehike(cls,percentage):
        cls.emphike=percentage

    def showsalary(self):
        self.salary=self.salary+self.salary*(self.emphike/100)
        print(f"salary of {self.name} is {self.salary}")

e1=Employee("Amogh",90000)
e2=Employee("Vaishali",100000)

e1.showsalary()
e2.showsalary()

print(e1.salary)

e1.employeehike(20)
print("\n")

e1.showsalary()
e2.showsalary()


print("--------------------------------------------")
"""Super Method"""
print("\n")

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello {self.name}")

class Developer(Employee):
    def __init__(self,name,age,language):
        self.language=language
        super().__init__(name,age)

    def greet(self):    # Method override
        super().greet()     # calling greet method from parent class
        print(f"Our {self.language} developer")

e1=Developer("Amogh",28,"SQL")
e1.greet()
Employee.greet(e1)


print("--------------------------------------------")
"""Private access specifiers"""
print("\n")

class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __showstudentdetails(self):
        print(f"Name of the student is {self.__name} and age is {self.__age}. This is printed from Parent class")

class Csstudent(Student):

    def __init__(self,name,age):
        super().__init__(name,age)

    def showstudentdetails(self):
        super()._Student__showstudentdetails()  # super().___Student__showstudentdetails() will not work
        print("Above stmt from child class")

s1=Csstudent("amogh",12)
# s1.__showstudentdetails() # returns error
s1._Student__showstudentdetails()   # call for parent class method
s1.showstudentdetails()     # call for child class method

s2=Student("Vaishali",34)
print(s2._Student__name)    # s2.name cant be accessed directly


print("--------------------------------------------")
"""Protected access specifiers"""
print("\nProtected class------------------")

class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def _showstudentdetails(self):
        print(f"Name of the student is {self._name} and age is {self._age}")

class Csstudent(Student):

    def __init__(self,name,age):
        super().__init__(name,age)

s1=Csstudent("amogh",12)
s1._showstudentdetails()

s2=Student("Vaishali",34)
print(s2._name)


print("--------------------------------------------")
"""Multiple Inheritance"""
print("\n")


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_employee_details(self):
        print(f"Name of the employee is {self.name}")

class Salary:
    def __init__(self,salary):
        self.salary=salary

    def show(self):
        print(f"Salary of the employee is {self.salary}")

class Employeesalary(Salary,Employee):
    def __init__(self, salary, name, age):
        super().__init__(salary)
        self.name=name
        self.age=age

    def show(self):
        super().show()
        self.show_employee_details()

e1=Employeesalary(90000,'Amogh',28)
print(e1.name,"\n")
e1.show_employee_details()
print("\n")
e1.show()


print("--------------------------------------------")
"""Multilevel Inheritance"""
print("\n")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person_details(self):
        print(f"\nName: {self.name} \nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position=position

    def show_employee_details(self):
        super().show_person_details()
        print(f"Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, age, position, department):
        super().__init__(name, age, position)
        self.department=department

    def show_manager_details(self):
        super().show_employee_details()
        print(f"Department: {self.department}")

m1=Manager("Prashanth",58,"General Manager","Quality")
m1.show_manager_details()


print("--------------------------------------------")
"""Operator overloading"""
print("\n")

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth

    def __lt__(self, other):
        return self.area() < other.area()

r1=Rectangle(10,8)
r2=Rectangle(20,10)
print(r1<r2)


print("--------------------------------------------")
"""Walrus Operator"""
print("\n")

a=[1,2,3,5,6,7,8]

while (i:=len(a))>0:
    print(a[i-1])
    a.pop()

print("--------------------")

a=[]
b=[]
while(i:=input("Enter you favourite snacks:")) != "quit":
    a.append(i)

for string in a:
    if ((length:=len(string))>4):
        b.append(string)

print(b)


print("--------------------------------------------")
"""Opeartor Overloading"""
print("\n")

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __lt__(self, other):
        return self.salary < other

e1=Employee("amogh",25000)
print(e1<26000)


print("--------------------------------------------")
"""Generators"""
print("\n")

def fib_generator(n):

    a=0
    b=1
    i=0

    while i < n:
        yield a
        a,b = b,b+a
        i =i+1

a=fib_generator(5)
for num in a:
    print(num)


"""Match case"""
print("\n")

age=0

match age:

    case age if age >= 18 :print("You can drive")
    case age if age < 18 and age>0 : print("You cannot drive")
    case _:print("this is the default case. Enter your correct age")

print("\n")

# Short hand If Else

x=10
y=20

print("x>y") if x>y else print("y>x") if y>x else print("x=y")

print(c:= x if x>y else y if y>x else 0)

print("--------------------------------------------")
""""""
print("\n")

