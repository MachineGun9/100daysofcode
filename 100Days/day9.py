# dictionary
empty_dictionary = {}  # empty dictionary

print(empty_dictionary)

capitals_dictionary = {
    "India": "New Delhi",
    "USA": "Washington",
    "Italy": "Rome"
}

print("-" * 80)

print(capitals_dictionary)  # print complete dictionary

print(capitals_dictionary["India"], capitals_dictionary["USA"])  # print value for particular key

# key need to same as in dictionary, like rome is not equal to Rome.

# Dictionary key must be immutables, like string, tuple, numbers. When providing string as key remember to use "" or ''
# dictionary value can be any data type

print("-" * 80)

dictionary_one = {
    (1, 2, 3): "a tuple key", # Key as a tuple
    999: "a number key",
    "Hello": "a string key"
    # [1, 2]: "Musical note C#" # this key setup will give error
}

print(dictionary_one[(1, 2, 3)])
print(dictionary_one["Hello"])
print(dictionary_one[999])

print("-" * 80)

dictionary_two = {
    "ice_cream": ["vanilla", "butter scotch", "chocolate", "tutti fruity", "strawberry"],
    "rivers": {"Ganga": "India", "Nile": "Egypt", "Amazon": "Brazil"},
    "Animals": [["Lion", "Tiger"], ["Deer", "Rabbit"]]
}

# way access nested elements. concatenate key, position
print(dictionary_two["ice_cream"][0]) # vanilla
print(dictionary_two["rivers"]["Ganga"]) # India
print(dictionary_two["Animals"][1][1]) # Rabbit

print("-" * 80)

# key values can't be modified. content/ values can be modified

dictionary_three = {
    "Gender": ["M", "F", "O"],
    "Planets": ["Earth"]
}

print(dictionary_three["Planets"])
dictionary_three["Planets"].append("Mars")
print(dictionary_three)

# iterate ove dictionary

for i in dictionary_three: # this will print just keys
    print(i)

for i, j in dictionary_three.items(): # will print key value in pairs
    print(i, j)

for j in dictionary_three.values(): # will print just values
    print(j)

print("-" * 80)

# to delete a key value pair, use del or pop

del dictionary_three["Gender"] # will delete Gender
print(dictionary_three)

dictionary_three.pop("Planets")
print(dictionary_three)

print("-" * 80)

# another way to create a dictionary
dictionary_four = dict(
    Manager="Tony",
    Employeer="Rita",
    HR="Mike")
print(dictionary_four)

dictionary_five = {
    "CEO": "Steve",
    "CFO": "Ricky",
    "CIO": "Robert",
    "Manager": 'Tim',
    "HR": "Shiela"
}

# it will use another dictionary and append into current. beware,
# if keys are same in wto dictionary it will replace key/value of first dict with second one.
dictionary_five.update(dictionary_four)
print(dictionary_five)

print("-" * 80)

# in pythion when assign one list/dict to another it is a shallow copy, means memory address is same for both
# to create different lists in memory use "import copy" ans copy.copy(iterable) or copy.deepcopy(iterable)

import copy
# dictionary_six = dictionary_five # shallow copy
dictionary_six = copy.copy(dictionary_five) # deep copy

print(id(dictionary_five), " | ", id(dictionary_six))

dictionary_five["CEO"] = "Martin"

print(dictionary_five)
print(dictionary_six)

# in case of list as well

list_one = [1, 2, 3]

# list_two = list_one # shallow
list_two = copy.copy(list_one) # deep

print(id(list_one), " | ", id(list_two))

list_one.append(4)

print(list_one, list_two)

list_two.append(5)

print(list_one, list_two)

print("-" * 80)

dictionary_seven = {}
dog = "Rex"
cat = "Fluffy"
dictionary_seven["Dog"] = dog
dictionary_seven["Cat"] = cat

print(dictionary_seven)