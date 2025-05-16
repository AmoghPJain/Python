"""
Decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method
without modifying its source code.
It takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.
"""

def greet(fx):      #for functions without arguments
    def mfx():
        print("\nGood Morning")
        fx()
        print("Thanks for using this function\n")
    return mfx


def greet1(fx):     #for functions with arguments
    def mfx(*arg):
        print("Good Morning")
        fx(*arg)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World!")

def add(a,b):
    print(a+b)

@greet1
def sub(a,b):
    print(a - b)

hello()
add(1,2)
sub(5,8) #This will not work as fx in greet function does not take any arguments


print("\nPractical use case------------------------------")

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
    return decorated

@log_function_call
def my_addfunction(a, b):
    return a + b

my_addfunction(10,22)