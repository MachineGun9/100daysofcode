# caesar cipher

def shift_alphabet(shift_count):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alphabet[shift_count:] + alphabet[:shift_count]
    return str.maketrans(alphabet + alphabet.lower(), shifted + shifted.lower())


def caesar_cipher(input_message, shift_count):
    translation_table = shift_alphabet(shift_count)
    return input_message.translate(translation_table)


def caesar_decipher(encoded_message, decoding_num):
    return caesar_cipher(encoded_message, -decoding_num)


print("Welcome to the Caesar Cipher Program")

while True:
    method = input("Type 'encode' to cipher and 'decode' to decipher: ").lower()
    if method in ['encode', 'decode']:
        break
    else:
        print("Invalid input")

while True:
    text = input(f"Enter your message to be {method}d: ")
    if len(text) > 0:
        break
    else:
        print("Please enter a message.")

while True:
    try:
        shift = int(input("Enter the shift number: "))
        break
    except ValueError:
        print("Input must be a number")

if method == 'encode':
    print(f"The {method}d text is: {caesar_cipher(text, shift)}")
else:
    print(f"The {method}d text is: {caesar_decipher(text, shift)}")