"""
Generators are a special type of function in Python that allows you to create iterators in a more concise and memory-efficient way.
Instead of returning all the values at once like a regular function, a generator yields values one at a time, ON DEMAND.
It is more memory efficient, improved performance
"""

def my_generator(n):
    """A generator function that yields numbers from 0 to n-1."""
    i = 0
    while i < n:
        yield i
        i += 1

# Create a generator object
gen = my_generator(5)

# Iterate over the generated values using next()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

for value in gen:
    print("from for loop")
    print(value)  # Output: 0, 1, 2



def read_large_file(file_path):
    """Generator to read a large file line by line."""
    with open(file_path, "r") as file:
        for line in file:   #Instead of reading the entire file at once (e.g., with file.readlines()), each line is read one at a time, which is efficient for large files.
            yield line.strip()  # Yield each line (without newline characters by using strip function)

# Example usage
for line in read_large_file("large_file.txt"):
    print(line)  # Process each line (e.g., display or analyze)

def fibonacci_generator(n):
    a=0
    b=1

    for i in range(n):
        yield a
        a,b=b,b+1

fib_gen = fibonacci_generator(6)
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))

print("\n")
for i in range(3):  # Get the first 10 Fibonacci numbers
    print(next(fib_gen))
