# function in python
import random

# simple function to test functionality
def my_function():
    print("Hello World")
    print("checking my new function")

my_function() # call function

# Indentation in python: using 4 spaces for indentation is recommended by official python

# while loop - executes until condition is true.
# this code will run indefinitely as it will never get false. to stop either use make cond
# false or break the loop
while True:
    print("Hello")
    if random.randint(1,10) == 6:
        break


