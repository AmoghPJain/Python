x=4 #global variable
print(f"\nValue of global variable x = {x}")

def hello():
    x=10    #local variable
    print(f"\nValue of local variable x = {x}")
    y=5
    print(f"Value of local variable y = {y}")

hello()

print(f"\nValue of global variable x = {x}")
# print(f"Value of local variable y = {y}") This will give error as "y" can be accessed only from hello function


print("\n-------------------------------------------")
a = 10 # global variable
print(f"\nValue of global variable a = {a}")

def my_function():
  global a
  a = 5 # this will change the value of the global variable x
  print(f"Value of local variable a = {a}")

my_function()

print(f"Value of global variable a = {a}")
