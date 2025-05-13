import os

# if not os.path.exists("C:/Amogh/Python"):
#     os.mkdir("C:/Amogh/Python")         #creates a folder Python
#
# for i in range(0,100):
#     os.mkdir(f"C:/Amogh/Python/Day {i}")        #creates day0-day100 folders inside python
#
# for i in range(0,100):
#     os.rename(f"C:/Amogh/Python/Day {i}",f"C:/Amogh/Python/Python {i}")  #renaming all the folders from day to python

print("\n", os.getcwd())

folders=os.listdir("C:/Amogh/Python/")
print(folders)      #to list the folders/files inside the Python folder, returns a list

# for folder in folders:
#     print(folder)

print("\n")

for folder in folders:
    a=os.listdir(f"C:/Amogh/Python/{folder}")
    print(folder,a) #printing the contents inside each folder

# os.rmdir(path) - for removal of empty directories
# os.remove(path) - for removal of files

"""
os.getcwd()
os.path.exists("C:/Amogh/Python")
os.mkdir("C:/Amogh/Python")     #to rename any file/directory
os.listdir("C:/Amogh/Python/")
os.rmdir(path)      # to remove empty directories
os.remove(path)     # to remove files
os.rename(old_file,new_file)
"""

print("\nShutil module----------------------------------------------")

import time
import shutil

if not os.path.exists("C:/Amogh/Python/ShutilModlule"):
    os.mkdir("C:/Amogh/Python/ShutilModlule")

with open("C:/Amogh/Python/ShutilModlule/test.py","w") as f:    # creating a file
    pass

shutil.copy("C:/Amogh/Python/ShutilModlule/test.py","C:/Amogh/Python/ShutilModlule/test1.py",)  # to copy single file
shutil.copytree("C:/Amogh/Python/ShutilModlule","C:/Amogh/Python/ShutilModlule1")   # to copy multiple files or folder structure
time.sleep(20)
shutil.move("C:/Amogh/Python/ShutilModlule1/test1.py","C:/Amogh/Python/ShutilModlule/test2.py")     # to move files
shutil.rmtree("C:/Amogh/Python/ShutilModlule1")     # to delete a folder

time.sleep(20)

shutil.rmtree("C:/Amogh/Python/ShutilModlule")

"""
shutil.copy(f1,f2)		# to copy single file
shutil.copytree(a,b)	# to copy multiple files or folder structure
shutil.rmtree(a,b)	 	# to delete a folder
shutil.move(f1,f2)		# to move files
"""