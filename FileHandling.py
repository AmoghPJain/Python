import os

print(os.getcwd())

if not os.path.exists("C:/Amogh/Python/PythonFileHandling"):
    os.mkdir("C:/Amogh/Python/PythonFileHandling")

# #appending a file
f=open('C:/Amogh/Python/PythonFileHandling/MyFile.txt','a')
f.write(", you are awesome\n")
f.close()

filepath="C:/Amogh/Python/PythonFileHandling"

# writing a file
f=open("C:/Amogh/Python/PythonFileHandling/marks.txt","w")
f.write("90,83,95\n93,34,53\n82,56,85\nAmogh\nVaishali")
f.close()

# reading all the lines in a file
f=open("C:/Amogh/Python/PythonFileHandling/marks.txt","r")
lines=f.readlines()

for line in lines:
    print(line.strip())
f.close()

"""
Read() VS readlines():

read returns a single string containing the entire content of the file. Best for small files where you want to process all the content at once.
readlines returns entire content of a file as a list of lines. You can use it whenever you want to process the data line by line

"""
# -----------------------------------------------------------

# Another method for file handling
with open('C:/Amogh/Python/PythonFileHandling/MyFile.txt','r') as f:
    print(f.read())

    
with open("C:/Amogh/Python/PythonFileHandling/file.txt",'w') as file:
    file.write("Amogh is a good boy")

with open("C:/Amogh/Python/PythonFileHandling/file.txt",'r') as file:
    data=file.read(5)       #reads 5 characters
    print(data)

    file.seek(5)            #skips first 5 characters and points to 6th character
    data=file.read()        #reads from 6th character
    print(data)

with open("C:/Amogh/Python/PythonFileHandling/file.txt", 'w') as file:
    file.truncate(5)    #this will keep only starting 5 characters in the file and truncate the rest

def print_folder_with_files(folder_path):
    for root, _, files in os.walk(folder_path):
        if files:  # Check if there are files in the current folder
            print(f"Folder: {root}")
            print("Files:")
            print(f"    {files}")
            print()  # Blank line for better readability

# Replace "Python" with the path to your folder
folder_path = "C:/Amogh/Python/"
print_folder_with_files(folder_path)

with open("C:/Amogh/Python/PythonFileHandling/marks.txt","r") as f:
    f.seek(5)
    print(f.read())

"""
f=open(path,mode)
f.close()
f.read()
f.write("")
f.readline()
f.seek(5)
file.truncate(5)
"""