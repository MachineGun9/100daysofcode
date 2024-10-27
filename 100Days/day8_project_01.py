# caesar cipher

def shift_function(shift_count):
    english_alphabets = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    english_alphabets_shifted = english_alphabets[shift_count:] + english_alphabets[:shift_count]

    return english_alphabets, english_alphabets_shifted

def caesar_cipher(input_message, encoding_num):
    # get the shifted alphabet list
    english_alphabets, english_alphabets_shifted = shift_function(encoding_num)
    print(english_alphabets, english_alphabets_shifted)
    cipher_text = []
    for character in input_message:
        if character.isupper():
            char_index = english_alphabets.index(character)
            cipher_text.append(english_alphabets_shifted[char_index])
        elif character.islower():
            char_index = english_alphabets.index(character.upper())
            cipher_text.append(english_alphabets_shifted[char_index].lower())
        else:
            cipher_text.append(character)


    return "".join(cipher_text)

# in cipher we shifted alphabets by n place forward. in decipher we need to shift alphabets reverse by n.
#  i.e in cipher, if we shift by 9, we place H inplace of Q. When doing decipher we need Q in place of H. therefore
#  we need to shift by -9 now.
def caesar_decipher(encoded_message, decoding_num):
    return caesar_cipher(encoded_message, -decoding_num)


print("Welcome to the Caesar Cipher Program")

while True:
    method = (input("Type 'encode' to cipher and 'decode' to decipher: ")).lower()
    if method not in ['encode', 'decode']:
        print("Invalid input")
        continue
    else:
        break

while True:
    text = (input(f"Enter you message to be {method}d: "))
    if len(text) == 0:
        print("Please enter a message: ")
        continue
    else:
        break


while True:
    try:
        shift = (int(input("Enter the shift number: ")))
    except ValueError:
        print("Input must be a number")
    else:
        break

if method == 'encode':
    print(f"The {method}d text is: {caesar_cipher(text, shift)}")
elif method == 'decode':
    print(f"The {method}d text is: {caesar_decipher(text, shift)}")


