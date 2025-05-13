"""
The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression.
This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.
"""
print(happy:=True)
print(happy)

numbers=[1,2,3,4,5]

while (i:=len(numbers)) > 0:
    print(numbers.pop())

print("\n")
# it could have been written as below without the walrus operator
numbers=[1,2,3,4,5]

i=len(numbers)
while i > 0:
    print(numbers.pop())
    i = i-1

print("\n")

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)