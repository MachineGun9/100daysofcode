import random
# The dictionary
a = {
    'player1': ['value1', 'value2', 'value3'],
    'player2': ['value4', 'value5', 'value6'],
    'player3': ['value7', 'value8', 'value9'],
}

# Key for which we want to remove a value
key_to_modify = 'player1'
# Value to remove
value_to_remove = 'value2'

random_key = random.choice(list(a.keys()))
print(random_key)

value = (random.choice(a[random_key]))

a[random_key].remove(value)

print(a)


# Check if the key exists in the dictionary and the value exists in the list
# if key_to_modify in a and value_to_remove in a[key_to_modify]:
#     a[key_to_modify].remove(value_to_remove)
#
# print(a)
