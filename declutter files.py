import os

if not os.path.exists("C:/Amogh/Python/Declutter"): # if path is not present, create a new path
    os.mkdir("C:/Amogh/Python/Declutter")

for i in range(1,6):    # creating files

    if not os.path.exists(f"C:/Amogh/Python/Declutter/python{i}.py"): # create a file if it is not present
        with open(f"C:/Amogh/Python/Declutter/python{i}.py","w") as f:
            f.write("")

    if not os.path.exists(f"C:/Amogh/Python/Declutter/test{i}.txt"): # create a file if it is not present
        with open(f"C:/Amogh/Python/Declutter/test{i}.txt","w") as f:
            f.write("")

def rename_file(path,type):

    file_list=[f for f in os.listdir(path) if f.endswith(type)]
    print(file_list)

    for i,f in enumerate(file_list,start=1):     #to rename all the files present in the list(file)

        if f.endswith(type):
            print(f)
            os.rename(f"{path}/{f}",f"{path}/{i}.{type}")


a=rename_file("C:/Amogh/Python/Declutter","txt")
