name="Amogh"

for i in name:
    print(i)
    if(i=="h"):
        print("This is the end of name\n")

colours=["Red","Green","Blue"] #list
for colour in colours:
    print(colour)
    for i in colour:
        print(i)
    print("\n")

for k in range(5): #range is used to generate sequence of numbers, commonly used in loops
    print(k) #0-4
print("\n2:")

for k in range(5):
    print(k+1) #1-4
print("\n3:")

for k in range(1,5):
    print(k) #1-5
print("\n4:")

for k in range(1,8,3):
    print(k) #1,4,7
print("\n5:")

for i in range(10, 4, -2):  # Negative step for reverse order
    print(i) #10,8,6


print("\nLets apply break condition------------------ ")

for i in range(12):
    if(i==5):
        break #if i=10, it exits the for loop
    print("5 *",i,"=",5*i)
print("skipped the loop")

print("\nLets apply continue condition------------------ ")

for i in range(6):
    if(i==0):
        continue #if i=0, it skips whatever is there below the keyword "continue" inside the loop. after skipping for the given condition, it continues with the loop
    print("5 *",i,"=",5*i)
print("skipped the iteration for i = 0\n")


for i in [2,3,4,6,8,0]: #list
    if (i%2 != 0):
        continue
    print(i) #prints only even numbers


# Enumerate function
print("\nEnumerate function")

marks=[34,65,39,84,93]
index= 0

for mark in marks:
    print(mark)
    if(index==2):
        print("Amogh")
    index +=1

print("\n")

for index,mark in enumerate(marks):
    print(mark)
    if(index==2):
        print("Amogh")
    index +=1

    # Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits,start=1):
    print(index, fruit)

#use REVERSED for printing in reverse order
for fruit in reversed(fruits):
    print(fruit)

print("\n")

#Conditional filtering using FOR loop
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
print("\nnames =",names)

namesWith_O = [item for item in names if "o" in item]
print("\nNames containing o:",namesWith_O)

name4 = [item for item in names if (len(item) > 4)]
print("Names having at least 5 characters in them:",name4)