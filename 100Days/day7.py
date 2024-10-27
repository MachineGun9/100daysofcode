# hangman project day
# no training

# enumerate
import random
fruits_in_basket = ["Apple", "Banana", "Grapes", "Oranges", "Pear", "_", "_"]
fruits_string = "".join(fruits_in_basket)
print(fruits_string)


# for index, fruit in enumerate(fruits_in_basket):
#     print(index, fruit)

not_guessed_indexes = [i for i, letter in enumerate(fruits_in_basket) if letter == "_"]
print(not_guessed_indexes)

hint_index = random.choice(not_guessed_indexes)
print(hint_index)

print(fruits_string[hint_index])