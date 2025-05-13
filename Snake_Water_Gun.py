import random

user=int(input("Choose between Snake Water or Gun, 1 for Snake, 2 for Water and 3 for Gun:"))
comp=random.randint(1,3)

# S W G

a=[]
a.append(user)
a.append(comp)

l=[[1,1],[1,2],[1,3],
   [2,1],[2,2],[2,3],
   [3,1],[3,2],[3,3]]

i1=[]
i2=[]

if a in (l[1],l[5],l[6]):
    print("\nUser wins")
elif a in (l[0],l[4],l[8]):
    print("\nIt is draw")
else:
    print("\nComp wins")
