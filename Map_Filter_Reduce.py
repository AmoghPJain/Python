# Map
print("\nMap--------------------------------------------")

def cube (x):
    return x*x*x

l=[1,3,56,8,4]

newl=[]
for i in l:
    newl.append(cube(i))

print("1",newl)

# Now instead of above we can use MAP to apply the function for each item in l
# map takes function and any iterable object as parameters

a=list(map(cube,l))
print("2",a)

a=list(map(lambda x:x*x*x,l))
print("3",a)

# Filter

print("\nFilter--------------------------------------------")
def filternum(x):
    return x>3  # returns true if x>3

b=list(filter(filternum,l))
print("1",b)

b=list(filter(lambda x: x>3, l))
print("2",b)

print("\nReduce--------------------------------------------")

from functools import reduce

def mysum(x,y):
    return x+y

c=reduce(mysum,l)
print("1",c)

d=reduce(lambda x,y:x+y,l)
print("2",d)