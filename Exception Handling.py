"""
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
Exception handling deals with these events to avoid the program or system crashing, and without this process,
exceptions would disrupt the normal operation of a program.
"""

try:
    num = int(input("Enter an integer: "))
    print("It is a Valid number")
except :
    print("Number entered is not an integer.")

try:
    num = int(input("Enter an integer: "))
    print("It is a Valid number")
except Exception as e:
    print(e)


"""
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. 
The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection.
One of the important use cases of finally block is in a function which returns a value.
"""

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Valid integer")
finally:
    print("This block is always executed.")
print("This block also is always executed.") # why to use finally block when we can print like this. the answer is below


def func1():
    try:
        l=[1,2,3,4]
        print("l =",l)

        a=int(input("Enter a index value:"))
        print(l[a])
        return 1

    except:

        print("this is not a valid integer")
        return 0

        #if finally was not present in the function it would have directly returned 1/0 and wouldn't have executed other part of the function
    finally:
        print("I am always executed")           #This can be used for any cleanup activities

x=func1()
print(x)

print("Custom error------------------------")

a=int(input("Enter any values between 5 and 9:"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")