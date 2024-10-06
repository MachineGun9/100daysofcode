import random
from string import ascii_lowercase as letters, digits

print(letters)
print(digits)

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

print("Welcome to the password generator!")
while (count_letter := int(input("How many letter you want in pwd? "))) < 4:
    print("The number of letter must be greater than 3!")

while (count_digit := int(input("How many digit you want in pwd? "))) < 4:
    print("The number of digit must be greater than 3!")

while (count_special_char := int(input("How many special character you want in pwd? "))) < 2:
    print("The number of special character must be greater than 2!")

list_for_pwd = (
    [random.choice(letters) for _ in range(count_letter)] +
    [random.choice(digits) for _ in range(count_digit)] +
    [random.choice(special_characters) for _ in range(count_special_char)]
)

random.shuffle(list_for_pwd)

suggested_pwd = ''.join(list_for_pwd)

print(f"suggested password: {suggested_pwd}")