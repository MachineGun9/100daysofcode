# function

def my_function(name, age): # positional parameters, need to be same order when called function.
    print("Hello", name, "your age is ", age)

# function is called using values swapped in position, results are incorrect as per expectation
my_function("Bob", 25) # output : Hello Bob your age is  25
# if variables provide incorrect, results gets weird
my_function(25, "Bob") # output : Hello 25 your age is  Bob

# if a variable is missed in function call you will get error
# to prevent this use default value in function if possible. in function definition variables can be defaulted.
# Default parameter must be followed by non default. it is to maintain function call syntax correct

def calculate_profit(cost , sell = 35):
    profit = sell - cost
    return profit

print("profit: ", calculate_profit(25, 35)) # profit:  10
# if we leave sell value, it will take default from definition
print("profit: ", calculate_profit(30)) # profit:  5.

# Keyword parameter. to prevent positional parameter order issue, keyword parameters can be used instead.
# order doesn't matter in this case.

def who_cooked_whom(chef, livestock):
    print(chef, "cooked ", livestock, " delicious.")

who_cooked_whom("Mike", "Chicken") # Mike cooked  Chicken  delicious.

who_cooked_whom("Lion", "Shelly") # Lion cooked  Shelly  delicious. looks weird but can be true :)

who_cooked_whom(livestock = "Lion", chef = "Shelly") # Shelly cooked  Lion  delicious. keyword param save Shelly.



