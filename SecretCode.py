"""
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

Coding:
if the word contains at least 3 characters, remove the first letter and append it at the end
  now append three random characters at the starting and the end
else:
  simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
 Your program should ask whether you want to code or decode
"""

rand1="dsf"
rand2 ="hkr"
newword=[]

def encode(a):
    words=a.split(" ")

    for word in words:
        if(len(word)>=3):
            b=rand1+word[1:]+word[0]+rand2
        else:
            b=word[::-1]
        newword.append(b)

    print(" ".join(newword))


def decode(a):
    words=a.split(" ")
    newword=[]
    for word in words:
        if len(word)>=3:
            b=word[3:-3]
            c=b[-1]+b[0:-1]
        else:
            c=word[::-1]
        newword.append(c)

    print(" ".join(newword))

inp=100 #random value other than 1 or 2
while(inp!=1 and inp!=2):  #This runs in loop till the user gives the right option

    inp=int(input("\nSelect 1 for encoding and 2 for decoding:"))
    if (inp != 1 and inp != 2):
        print("Enter a valid input")

if inp == 1:
    str=input("\nEnter your value for encoding:")
    encode(str)
else:
    str = input("\nEnter your value for decoding:")
    decode(str)

