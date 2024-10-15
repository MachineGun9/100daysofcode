# hangman game Rules:
# Choose a Word: One player selects a word and writes a series of underscores on a board or paper, representing each letter of the word.
# Guess Letters: The other player guesses letters one at a time.
# Correct Guess: If the guessed letter is in the word, fill in the blanks with the correctly guessed letter in all its positions within the word.
# Incorrect Guess: If the guessed letter is not in the word, draw one part of the hangman figure.
# Winning: The player wins if they guess all the letters in the word before the hangman figure is completely drawn.
# Losing: The player loses if the hangman figure is completely drawn before the word is guessed.
import random
from random import randint


def choose_word():
    words = [
        'python', 'algorithm', 'hangman', 'challenge', 'programming',
        'function', 'variable', 'exception', 'iteration', 'development',
        'object', 'class', 'syntax', 'compilation', 'debugging',
        'inheritance', 'polymorphism', 'encapsulation', 'abstraction',
        'interface', 'dictionary', 'list', 'tuple', 'set',
        'library', 'module', 'script', 'syntax', 'runtime',
        'coding', 'software', 'hardware', 'network', 'database',
        'server', 'client', 'protocol', 'encryption', 'security',
        'performance', 'optimization', 'testing', 'deployment', 'version',
        'control', 'repository', 'branch', 'merge', 'commit',
        'pull', 'push', 'clone', 'fork', 'build',
        'continuous', 'integration', 'testing', 'automation', 'pipeline'
    ]
    return random.choice(words)

# hangman portrait

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

CONGRATS = '''
                                 _       
                                | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \\| '_ \\ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\\__ \\
 \\___\\___/|_| |_|\\__, |_|  \\__,_|\\__|___/
                  __/ |                  
                 |___/ 
'''
LOOSE = '''
 _           _   
| |         | |  
| | ___  ___| |_ 
| |/ _ \\/ __| __|
| | (_) \\__ \\ |_ 
|_|\\___/|___/\\__|
'''

print("Welcome to the Hangman Game!")
print("you have 7 chances to guess the word!")
print(HANGMAN[0])


chosen_word = choose_word()
chosen_word_len = len(chosen_word)
chosen_word_list = ['_'] * chosen_word_len

print(chosen_word)

guessed_letters = set()

print("Start Guessing...")
print("Word to guess: " + "alphabets = " + str(chosen_word_len) + " : " + ' '.join('-' for _ in chosen_word_list))

user_chances = len(HANGMAN) - 1
user_attempts = 0

hint_used = False

while user_attempts < user_chances:
    user_input: str = input("Guess a letter: ").lower()

    if user_input in guessed_letters:
        print("You have already guessed that letter. Try again.")
        continue
    else:
        guessed_letters.add(user_input)

    if len(user_input) != 1:
        print("Please enter a single letter.")
        continue

    if user_input in chosen_word:
        print("Good Job!")
        for i in range(chosen_word_len):
            if chosen_word[i] == user_input:
                chosen_word_list[i] = user_input

        print((' '.join(str(s) for s in chosen_word_list)))
    else:
        print("Oops! That letter is not in my word")
        user_attempts += 1
        print(HANGMAN[user_attempts])
        print("You have " + str(user_chances - user_attempts) + " chances left!")
        if user_attempts > int(user_chances/2):
            print("do you want a hint? ")
            if not hint_used:
                hint_used = True
                need_hint = input("y/n: ").lower()
                if need_hint == 'y':
                    for i in range(0, chosen_word_len, 3):
                        x = randint(0, chosen_word_len-1)
                        if chosen_word_list[x] == "_":
                            chosen_word_list[x] = chosen_word[x]
                else:
                    print("wrong choice. help ignored for now")

    print("Word to guess: " + "alphabets = " + str(chosen_word_len) + " : "
          + ' '.join(str(s) for s in chosen_word_list))

    if "_" not in chosen_word_list:
        print("You won!")
        print("The word was: " + chosen_word)
        print(CONGRATS)
        break
else:
    print("You lost!")
    print("The word was: " + chosen_word)
    print(LOOSE)
