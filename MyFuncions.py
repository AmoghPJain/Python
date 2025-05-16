"""
There are two types of functions:

Built-in functions
User-defined functions

Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs.
"""
print("\n")

def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print("calculategmean =",mean)

c=2
d=4

calculategmean(c,d)
calculategmean(3,6)

print("\n")

def calculategreatest(a,b):
    if a>b:
        print(a,"is greatest")
    else:
        print(b,"is greatest")

calculategreatest(100,20)

print("\nDifferent ways of calling a function-------------------------\n")

def calculatesmallest(a=200,b=100):
    if a < b:
        print(a, "is smallest")
    else:
        print(b, "is smallest")

print("\ncalculateSmallest(1,100):")
calculatesmallest(1,100)

print("\ncalculateSmallest(a=2):")
calculatesmallest(a=2)

print("\ncalculateSmallest(b=43):")
calculatesmallest(b=43)

print("\ncalculateSmallest():")
calculatesmallest()

def calculate_sum(numbers):

    return sum(numbers)

my_list = [10, 20, 30, 40, 50]
result = calculate_sum(my_list)
print(f"The sum of all numbers in the list is: {result}")

def printaverage(*numbers): #* will create a Tuple from the input that we give
    #print(type(numbers))
    sum=0

    for i in numbers:
        sum=sum+i

    print("\nAverage is:",sum/len(numbers))

printaverage(5,6) #can give as many numbers we want
printaverage(5,6,7)

def returnaverage(*numbers): #This function will return a value instead of printing
    #print(type(numbers))
    sum=0

    for i in numbers:
        sum=sum+i

    return sum/len(numbers)

c=returnaverage(5,2,3)

print("AVERAGE is:", c)

def name(**name):   #This will create a dict
    #print(type(name))

    print("\nHello,", name["fname"], name["mname"], name["lname"])

name(mname="Prashanth", fname="Amogh", lname="Jain")

"""
A lambda function is a small anonymous function without a name. It is defined using the lambda keyword
"""
print("Lambda Functions-----------------------\n")

add=lambda x,y: x+y
print(add(5,9))

print("\n")
average = lambda nums: sum(nums)/len(nums)

number=[1,2,45,6]
print(average(number))

# Docstrings------
"""
docstrings are the string literals that appear right after the definition of a function, method, class, or module.
"""

print("Docstrings example-----------------------\n")

def docstringex(a,b):
    """prints a+b"""
    print("Values = ",a+b)

print(docstringex.__doc__)


def docstringex1(a,b):
    print(1,2)
    """a+b"""
    print("Values = ",a+b)

print("\nThis docstring will not work")
print(docstringex1.__doc__)
