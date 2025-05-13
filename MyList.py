colours=["yellow","Green","Red","White","Lavender"]

print("\ncolours =",colours)
print("\nprint colours[3] =",colours[3])
print("print colours[-3] =",colours[-3])
print("print len(colours) =",len(colours))
print("print colours[1:3] =",colours[1:3])
print("print colours[0::2] =",colours[0::2]) #using JumpIndex

print("\nCheck if there are 6 elements in the colours list:")
if len(colours)==6:
    print("Yes")
else:
    print("No")

print("\nUsing FOR loop to print the list-------")
for colour in colours:
    print(colour)



a=[item for item in range(5)]
print(a)

list=list(range(5)) #converting range to a list
print("\nCreating a list using range()\n",list)

#List Comprehension
#List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print("\nnames =",names)

namesWith_O = [item for item in names if "o" in item]
print("\nNames containing o:",namesWith_O)

#items which have more than 4 letters
name4 = [item for item in names if (len(item) > 4)]
print("Names having at least 5 characters in them:",name4)


print("\nList Manipulations------------------------------------------------\n")

l=[11,45,1,1,2,4,6]
print("l =",l,"\n")

l.append(7)
print("l.append(7) =",l)

l.insert(0,88) #Adds 88 at the beginning
print("l.insert(0,88) =",l)

l.sort() #sorts ascending
print("l.sort() =",l)

l.sort(reverse=True)
print("l.sort(reverse=True) =",l) #sorts descending

l.remove(45)
print("l.remove(45) =",l) #sort descending

l=[11,45,1,1,2,4,6]
print("\nl=",l)
l.reverse()
print("l.reverse() =",l)

print("l.index(11) =",l.index(11)) #index returns the first occurrence of the given element.

print("l.count(1) =",l.count(1))

m=l.copy() # if u do m=l and do m[0] = 1, then values in m and l both will be changed. hence use copy method.
m[0]=0
print("\nm=l.copy() -> m[0]=0, m =:",m)

l.insert(1,899)
print("\nl.insert(1,899) =",l)

m=[900,1000,1100]

k=l+m   #or can be written as k=l.extend(m)
print("\nk = l+m; K =",k)

# Extend VS append
print("\nExtend VS Append\n")
# list.extend(iterable)

list1 = [1, 2]
list2 = [3, 4]

list1.extend(list2)  # Adds 3 and 4 individually
print("Extend :",list1)         # Output: [1, 2, 3, 4]

list1.append(list2)  # Adds `list2` as a single element
print("Append :",list1)         # Output: [1, 2, [3, 4]]


"""
l.copy()    # if u do m=l and do m[0] = 1, then values in m and l both will be changed. hence use copy method.
l.sort()
l.reverse()

l.index(1)  # To find out the location of the element. It returns the first occurance
l.count(45)
l.sort(reverse=True)
l.insert(1,"A")     # To insert an element in a particular index location

l.remove(value) # used to delete the first occurrence of a specific element from a list. It removes by value, not by index.
l.pop(index)    # Removes the element at the specified index and returns it, If no index is provided it removes and returns the last element.

l.extend(list1)
l.append("h")

To combine two lists:
a+b (Where a and b are lists)
"""