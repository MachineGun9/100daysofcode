#rock paper scissors
# ascii art for rock paper scissors. downloaded from GITHUB
# Rock
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to the Rock Paper Scissors game!")
print("-" * 80)
print("Here are your choices:")
print("r: Rock")
print("p: Paper")
print("s: Scissors")

while (user_selected_move := input("What is your choice? (r/p/s): ").lower()) not in ["r", "p", "s"]:
    print("Invalid move. Please try again.")

computer_choices = ["r", "s", "p"]

computer_selected_move = random.choice(computer_choices)

if user_selected_move == computer_selected_move:
    print("your move:" + user_selected_move)
    print("computer move:" + computer_selected_move)
    print("It's a tie :|")
elif user_selected_move == "r":
    if computer_selected_move == "s":
        print("your move:" + user_selected_move)
        print(rock)
        print("computer move:" + computer_selected_move)
        print(scissors)
        print("You won :)")
    elif computer_selected_move == "p":
        print("your move:" + user_selected_move)
        print(rock)
        print("computer move:" + computer_selected_move)
        print(paper)
        print("You loose :(")
elif user_selected_move == "p":
    if computer_selected_move == "r":
        print("your move:" + user_selected_move)
        print(paper)
        print("computer move:" + computer_selected_move)
        print(rock)
        print("You won :)")
    elif computer_selected_move == "s":
        print("your move:" + user_selected_move)
        print(paper)
        print("computer move:" + computer_selected_move)
        print(scissors)
        print("You loose :(")
elif user_selected_move == "s":
    if computer_selected_move == "p":
        print("your move:" + user_selected_move)
        print(scissors)
        print("computer move:" + computer_selected_move)
        print(paper)
        print("You won :)")
    elif computer_selected_move == "r":
        print("your move:" + user_selected_move)
        print(scissors)
        print("computer move:" + computer_selected_move)
        print(rock)
        print("You loose :(")