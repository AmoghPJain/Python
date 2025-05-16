i=int(input("Enter a number = "))

while(i<=3):
    print(i)
    i=i+1
else:
    print("\nNumber is > 3")

"""
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.
"""

print("\nEmulation of do While loop----------------------------\n")

while True: #must be an infinite loop
    number = int(input("Enter a positive number:"))
    print(number)
    if not number > 0:
        break