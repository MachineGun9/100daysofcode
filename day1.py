#day1
#string slice
print("HELLO WORLD"[::-1]) #index starts from 0 | start: The index where the slice begins (inclusive). stop: The index where the slice ends (exclusive). step: The interval between each character (optional).

#integer
num_int = 123 + 111
print(num_int)

#large int
large_int = 123456789
print(large_int)

#FLOAT
float_num = 1234.99 + 111.33
print(float_num)

#bool
bool_num = 1    # True/False OR 0/1
print(bool_num)

#type error: when provided wrong type of data to a method/func
#len(123) #TypeError: object of type 'int' has no len()

#type checking | type() operator
print("types of:", type("Hello"), " | ", type(123), " | ", type(123.45), " | ", type(False))

#conversion
num_from_str = int("123") #if try to enter string other than numbers err: ValueError: invalid literal for int() with base 10: 'Hello'
print(num_from_str)

str_from_int = repr(str(999)) #repr put inverted comma when displaying strings
print(str_from_int)

#Mathematic operations : expressions are evaluated from left to right. Divide and mul has equal priority. so left operation will be done first. not if brackets are there.
print(6 / 3 * 2)
print(6 * 3 / 2)

#BMI Calculator
height = 1.65
weight = 84

bmi = 84 / 1.65 ** 2

print(round(bmi, 2)) #round off floating values. mathematical round off. .133 round off to .13 & .138 round off to 1.4

# score = score + 1 can be written as score += 1

#f-strings - format strings more conveniently

print(f"Hello, your height is {height} meters, weight is {weight} KG. Your BMI is {bmi:.2f}")


