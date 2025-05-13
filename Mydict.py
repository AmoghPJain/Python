"""
In Python 3.7 onwards dictionaries are ordered.
Dictionary in Python can have duplicate values, but it cannot have duplicate keys.
"""

dict ={"name":"Amogh","city":"Bangalore","age":"28"}
print("\ndict =",dict)
print("dict[\"name\"] =",dict["name"])

print("\ndict.keys() =",dict.keys())
print("dict.values() =",dict.values())
print("dict.items() =",dict.items())

print("\n")

products = {
    "apple": 50,
    "banana": 30,
    "cherry": 20,
    "dates": 40
}

print(products)

# Use dict.values() to access the prices and calculate the total cost
total_cost = sum(products.values())

print(f"\nThe total cost of all products is: {total_cost}")

if 40 in products.values():
    print("A product priced at 40 is available.")

if "banana" in products.keys():
    print("Banana is available!\n")

# Iterate through the keys
for key in products.keys():
    print(f"Product: {key}")

print("\n")

a=[]    # creating a blank list
for i in dict.keys():
    a.append(dict[i])

print(a)    # creating a list from values

a=dict.keys()
b=dict.values()

print(type(a))
print(type(b))

print("\n")

for a in dict.keys():
    print(f"The value corresponding to the {a} is = {dict[a]}")

print("\n")

for key,value in dict.items():
    print(f"The value corresponding to the {key} is = {value}\n")

# for sorting
for key in sorted(dict.keys()):
    print(key)

#employee id, rating
mg1={122:45, 123:89, 567:69, 670:69}
mg2={222:67, 123:89, 566:90}

mg1.update(mg2) #Adds unique records
print(mg1)

mg1.pop(122)
print(mg1)

mg1.popitem()   #deletes last item from the dictionary
print(mg1)

del(mg2)     #deletes the ep2 dict

my_dict = {"name": "Alice", "age": 25}

print("my_dict =",my_dict)
my_dict["city"] = "New York"  # Add
my_dict["age"] = 26  # Update
print(my_dict)


"""
dict.keys()
dict.values()
dict.items()

mg1.update(mg2) # Adds unique records to mg1. mg1 and mg2 both are dictionaries
mg1.pop(122)	# here we need to pass the dictionary key
mg1.popitem()	# Removes and returns the last inserted key-value pair (python 3.7+)
mg1.clear()		# Removes all items from the dictionary
len(my_dict)	# Number of items in the dictionary

# dictionary in Python can have duplicate values, but it cannot have duplicate keys.
"""