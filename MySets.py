"""
Sets are UNORDERED collection of data items. Sets do not contain duplicate items.
The items in a set occur/displayed in random order and hence they cannot be accessed using index numbers.

Unordered, unchangeable, no duplicates
"""

info = {"Carla", 19, False, 5.9, 19}
print("\ninfo =",info)

a={}
print("\ntype(a) =",type(a))    # dict

b=set() #empty set
print("type(b) =",type(b))

s1={1,2,5,6}
s2={3,6,7}
print("\ns1 =",s1)
print("s2 =",s2)


print("\ns1.union(s2) =",s1.union(s2))              #displays union of both s1 and s2
print("s1.intersection(s2) =",s1.intersection(s2))  #intersection of elements from  s1 and s2

s1.update(s2)               #update s1 by adding elements from s2 which are not present in s1. It is different from union as here the set will be updated
print("s1 after s1.update(s2) =",s1)

s3={1,2,5,6}
s4={3,6,7}
print("\ns3 =",s3)
print("s4 =",s4)

s4.intersection_update(s3)
print("\ns4 after s4.intersection_update(s3) =",s4)

s3={1, 2, 3, 4}
s4={3, 4, 5}
print("\ns3 =",s3)
print("s4 =",s4)

print("\ns3.symmetric_difference(s4) =",s3.symmetric_difference(s4))      # returns a set containing elements that are in either of the sets but not in both.
print("s3.difference(s4) =",s3.difference(s4))      # same as A-B. elements which are present in the first set but not in the second set.
print("s3.isdisjoint(s4) =",s3.isdisjoint(s4))      # prints true if they have no element in common
print("s3.issuperset(s4) =",s3.issuperset(s4))      # prints true if all elements of s4 is present in s3
print("s2.issubset(s1) =",s2.issubset(s1))          # prints true if all elements of s2 are present in s1
s3.add(8)
print("s3.add(8) =",s3)
s3.remove(8)
print(" =",s3)
s3.discard(8)
print("s3.discard(8) =",s3)         # remove and discard have same functionality, only difference is that if you don't find an element, discard raises an error while remove method fails and exits the code
s3.clear()
print("s3.clear() =",s3)

"""
s1.union(s2)
s1.intersection(s2)
s3.add(8)
s3.remove(8)
s3.discard(8)
s1.update(s2)   # to add elements of s2 in s1 which are not present in s1
s4.intersection_update(s3)
s3.symmetric_difference(s4) # unique elements present in s3 and s4
s3.difference(s4)   #elements which are present in the S3 but not in the S4.
s3.isdisjoint(s4)
s3.issuperset(s4)
s2.issubset(s1)
"""