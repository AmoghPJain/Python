a="Amogh"
b="Vaishali"

print("\na =",a)
print("b =",b)

print("a+b =",a+b) #string concatenation example

print("\nPrint a[0] =",a[0])
print("Length of a =",len(a))

#print(a[5])  This will throw string out of range error

print("\nLets use FOR Loop")
for character in a: #Here character is used as a variable and instead of character you can use any other name as well
    print(character)


#Slicing
print("\nSlicing...........\n")

print("a =",a)

print("\na[0:4] =",a[0:4])  #prints from 0-3rd character
print("a[:4] =",a[:4])  #Slicing from start
print("a[2:] =",a[2:])  #Slicing till end
print("a[2:4] =",a[2:4])  #Slicing in between
print("a[:-2] =",a[:-2])  #Slicing using negative index. Same as a[0:len(a)-2]
print("a[4] =",a[4])
print("a[:] =",a[:])


#Negative Slicing
print("\nNegative Slicing.........\n")

print("a[0:-3] =",a[0:-3]) #Same as a[0:len(a)-2]
print("Above is same as a[0:len(a)-3] =",a[0:len(a)-3])

print("\na[-1:-3] prints nothing as it is same as a[4:2] and has no meaning,",a[-1:-3])#prints nothing, same as a[4:2]
print("a[-3:-1] =",a[-3:-1])

print("a.upper() =",a.upper())
print("a.lower() =",a.lower())

a="!!Amogh!!!"
print("\na =",a)
print("a.rstrip(\"!\") =",a.rstrip("!")) #removes any trailing character. NOTE it doesn't remove any trailing spaces like strip

a="!!Amogh!!!..."
print("\na =",a)
print("a.rstrip(\"!\") =",a.rstrip("!")) #It doesn't remove ! from variable an as it is not at trailing

#To replace entire string. Replaces all occurrence of a string with another string
a="Amogh......Amogh...aaa"
print("\na =",a)
print("a.replace(\"Amog\",\"Vaish\") =",a.replace("Amog","Vaish"))

print("\nsplit() method splits the given string at the specified instance and returns the separated strings as LIST......")
a="Amogh Vaishali"
print("\na =",a)
print("a.split(\" \") =",a.split(" "))
print(type(a.split(" ")))
print("a =",a) #Split doesnt update variable a


a="amogh,Vaishali"
print("\na =",a)
print("a.split(\",\") =",a.split(","))

#Camel Case
print("a.capitalize() =",a.capitalize())

a="Amogh.....Amogh..Vaishali"
print("\na =",a)
print("a.count(\"Amogh\") =",a.count("Amogh")) #Prints the count that has occurred in the string

#find searches for the first occurrence of the given value and returns the index. It cant be used for INT
print("a.find(\"g\") =",a.find("g"))    # returns -1 if no string is found
print("a.index(\"g\") =",a.index("g"))  # The major difference is that, index() raises an exception if value is absent whereas find() does not.

print("a.isalnum() =",a.isalnum()) #returns false because there are characters other than alphanumeric

a="Amogh1"
print("\na =",a)
print("a.isalpha() =",a.isalpha())

print("a.lower() =",a.lower())
print("a.islower() =",a.islower()) #returns True if all the characters in the string are lower case, else it returns False.
print("a.isspace() =",a.isspace()) #returns true if space exists
print("a.startswith(\"Amogh\") =", a.startswith("Amogh"))   #this method checks if the string starts with a given value
print("a.startswith(\"A\") =", a.startswith("A"))
print("a.isalnum() =", a.isalnum())


# Default behavior (removing whitespace)
text = "   Hello, World!   "
print("text =",text)
print("text.strip() =",text.strip())  # Output: "Hello, World!"
print("text.rstrip() =",text.rstrip())

# Removing specific characters
text = "###Python###"
print(text.strip('#'))  # Output: "Python"
print(text.rstrip('#'))

text = ",hello world!"
cleaned_text = text.strip(",!")
print(cleaned_text)


"""
a.upper()
a.lower()
a.islower()
a.isupper()
a.capitalize()
a.strip()
a.isalnum()
a.isalpha()

a.split(",")
a.rstrip("!")
a.count("g")
a.find("am")
a.index("am")
a.startswith("a")
a.endswith("gh")
a.replace("amo","Amo")

"""
