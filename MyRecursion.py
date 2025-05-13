#factorials----
#factorial(5) = 5*4*3*2*1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial(5) =",factorial(5))

def fibonacci(n):
    """
    This is a function which returns the fibonacci series of a given index
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci.__doc__)
print("fibonacci(6) =",fibonacci(6))