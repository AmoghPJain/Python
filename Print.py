#PRINT----------------------------------------------------------------------------

print("\nHello developer")
print("Hi", 7, 6)
print("Hi", 7, 6, sep="`")
print("Hi", 7, 6, sep="") #if you don't want spaces in between
print(17*12)

print("\nHello \"Amogh\"") #To display with double quotes
print("Hello \'Amogh\'") #To display with single quote

print("\nThis will \" execute")

# you can comment by using ctrl+/
# For MultiLine comment use ''' or """

'''
Comment1
Comment2
'''

"""
Comment1
Comment2
"""

a='''
We can use quotes
for multi-lined string
like this.
'''

print(a)

a="1" #string
b="3" #string

print("a+b=", int(a)+int(b))


print("\nf-strings-----------------------------------------------------------\n")

name="Amogh"
country="India"
print(f"\nHey my names is {name} and I am from {country}")

price=456.12354
print(f"\nYou owe me {price}Rs")
print(f"\nYou owe me {price:.2f}Rs") #to limit the number of decimalss