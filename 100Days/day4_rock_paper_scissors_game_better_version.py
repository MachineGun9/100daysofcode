import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

MOVES = {"r": ("Rock", ROCK), "p": ("Paper", PAPER), "s": ("Scissors", SCISSORS)}


def evaluate_game(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie :|"
    elif (user_move == "r" and computer_move == "s") or \
            (user_move == "p" and computer_move == "r") or \
            (user_move == "s" and computer_move == "p"):
        return "You won :)"
    else:
        return "You lose :("


print("Welcome to the Rock Paper Scissors game!")
print("-" * 80)
print("Here are your choices:")
for key, (name, _) in MOVES.items():
    print(f"{key}: {name}")

while (user_selected_move := input("What is your choice? (r/p/s): ").lower()) not in MOVES.keys():
    print("Invalid move. Please try again.")

computer_selected_move = random.choice(list(MOVES.keys()))

user_move_name, user_move_art = MOVES[user_selected_move]
comp_move_name, comp_move_art = MOVES[computer_selected_move]

print(f"Your move:\n{user_move_art}")
print(f"Computer move:\n{comp_move_art}")
print(evaluate_game(user_selected_move, computer_selected_move))
