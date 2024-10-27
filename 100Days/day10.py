# Function
# return output

def sum_function(a, b):
    return a + b

print(sum_function(2, 3))

#retrurn is last statement in function
# i.e.

def say_hello(name):
    print(f"Hello {name}")
    return
    print("I am Groot") # this statement will never execute

say_hello("Prateek")

def sentence_case(text):
    """this function will convert string to sentence case. like hello. -> Hello.""" # docstring
    uppercase_text = text[:1].upper() + text[1:].lower()
    return uppercase_text

print(sentence_case("hello."))

help(sentence_case) # when used help(function), docstring is displayed to help understand functionality.

def my_function_two(a, b, /, c, *, d, e):
    return [(a + b), (c*c), (d - e)]

print(my_function_two(1, 2, 3, d = 5, e = 0))


