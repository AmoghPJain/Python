age = int(input("Enter your age ="))
print("Your age is =",age)

#conditional operators
# >, <, >=, <=, ==, !=

print("\nage>=18 =",age>=18)
print("age<18 =",age<18)
print("age==18 =",age==18)
print("age!=18 =",age!=18)


print("\nIf else block started\n")

if age>=18:
    print("You can drive, age is above 17")
elif age==17:
    print("Try next year")
else:
    print("You cannot drive, wait till you become 18 years")
    #Nested if else
    if(age>0 and age<=10):
        print("\nNested block started\n")
        print("You are very small to learn driving")
    else:
        print("Wait for few years and learn")
    print("\nNested block ended")

print("\nIf else block ended")



print("\nMatch example............") #It is similar to SWITCH statement

match age:
    case 18:
        print("age = 18, you can drive")
    case age if(age>18):
        print("Person can drive(Match)")
    case age if(age>10 and age<18):
        print("Person cannot drive(Match)")
    case _:
        print("This is the default case:")


# If Else in one line..............

print("\nShort hand If Else................")

x=10
y=20

print("x>y") if x>y else print("y>x") if y>x else print("x=y")

print(c:= x if x>y else y if y>x else 0)
