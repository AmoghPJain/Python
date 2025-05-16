import time # imports entire time module

def timeofday():

    print(__name__)     #prints from which program this function is being called

    timestamp=time.strftime('%H:%M:%S') #need to add H,M,S in caps else it will not work
    print("\n",timestamp)
    print("\nDatatype of time is = ", type(timestamp))

    a=time.strftime('%H')
    print("\n")

    if int(a)<12:
        print("Good Morning")
    elif int(a) < 16:
        print("Good Afternoon")
    elif int(a) < 19:
        print("Good Evening")
    else:
        print("Good Night")

if __name__ == "__main__":
    timeofday()         # this function will be called only if it is executed from Timeprogram.py, if we try to import and run from other program, this will not execute

#-----------------------------------------------

from datetime import date, datetime     # in datetime module, imports date and datetime classes

print("\nToday's date is:", date.today())
print("Today's date and time is:", datetime.now())
print("Current time is:", datetime.now().time())
print("Current time is:", datetime.now().strftime("%H:%M:%S"))

print(date.today())
print(datetime.today())

a=time.time()
b=time.time()-a
print(b)


# # Add 1 year to today's date
from dateutil.relativedelta import relativedelta
one_year_later = date.today() + relativedelta(years=1)
print("Date after 1 year:", one_year_later)


# -----------------------------------------------

def print_numbers_with_while():

    start_time = time.time()  # Record the start time
    i = 0
    while i <= 5000:

        i += 1
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print("Time taken by while loop:", execution_time, "seconds")
    return execution_time #returning the execution time

def print_numbers_with_for():

    start_time = time.time()  # Record the start time
    for i in range(5001):

        pass # added pass, since you are not doing anything with i
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print("Time taken by for loop:", execution_time, "seconds")
    return execution_time #returning the execution time

if __name__ == "__main__":
    while_time = print_numbers_with_while()
    for_time = print_numbers_with_for()

    if while_time < for_time:
        print("While loop was faster")
    elif for_time < while_time:
        print("For loop was faster")
    else:
        print("Both loops took same time")