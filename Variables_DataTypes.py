
#Variables And DataTypes----------------------------------------------------------------------------

# A variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc

# IN PYTHON EVERYTHING IS STORED AS OBJECT. that is why type() returns class object

a=1
print("\na =",a)
print("type(a) =",type(a))

b=True #True is case-sensitive
print("\nb =",b)
print("type(b) =",type(b))

c="Amogh"
print("\nc =",c)
print("type(c) =",type(c))

d=None #None is case-sensitive
print("\nd =",d)
print("type(d) =",type(d))

# list : A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
# Lists are mutable(Changes allowed) and can be modified after creation.

list1=[1,2,-1,"Amogh",["Vaishali","Jain"]]
print("type(list1) =",type(list1))

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within round brackets.
# Tuples are immutable(Changes not allowed) and can not be modified after creation.

tuple2=(1,2,(2,4),"parrot",("Amogh","Vaishali"))
print("\nThis is a tuple", tuple2)
print("type(tuple2) =",type(tuple2))


#dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print("\nThis is a dictionary",dict1)
print("type(dict1) =",type(dict1))