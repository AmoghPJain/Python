"""
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets ().
Tuples are unchangeable meaning we can not alter them after creation.
"""

tup=(1)
print(type(tup))

tup=("sa")
print(type(tup))

tuple=tuple(range(5)) #converting range to a tuple
print(tuple,"------------")

tup=(1,) #when using only 1 value this will return int, add a "," to make it as a tuple
print(type(tup))

tup=(1,22,23,568,45)
print("\ntup =",tup)
print("tup[1] =",tup[1])
print("tup[-1] =",tup[-1])

print("\nCheck if value 22 is present in tup")
if 22 in tup:
    print("Yes")
else:
    print("No")

tup1=tup[2:4]
print("\ntup1 = tup[2:4]; tup1 =", tup1)

print("\nOperations on Tuple-----------------------------------------------\n")

tuple1=(0,1,2,3,4,3,2,3)
print("tuple1.count(3) =",tuple1.count(3))

count=0
for i in tuple1 :
    if(i!=3):
        continue
    else:
        count=count+1

print("\nCount of 3 =",count)

print("\nFirst occurrence of number 4 in tuple1 =",tuple1.index(4))

nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])      # Output: (2, 3)
print("nested tuple :",nested_tuple[1][0])   # Output: 2

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)


# Operations that can be done on a tuple:
"""
a[1]    # accessing
a[1:4]  # slicing
c=a+b   # concatenating two tuples
len(a)
a.count(3)
a.index(3)  # returns index of first occurrence of the value
min(a)
sum(a)
"""