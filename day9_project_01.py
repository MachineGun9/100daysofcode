# auction program.
import os
import subprocess
import day9_project_01_logo as logo

print(logo.logo)

# Ensuring TERM environment variable is set
def ensure_term():
    if 'TERM' not in os.environ or not os.environ['TERM']:
        os.environ['TERM'] = 'xterm-256color'


# Clearing Console
def clear_console():
    ensure_term()
    try:
        # Try using os.system
        if os.system('clear') != 0:
            # Fallback to subprocess methods if os.system fails
            subprocess.run(['clear'], check=True)
    except Exception:
        # Fallback to ANSI escape code
        print("\033c", end='')

print("Welcome to the Secret Auction program Ladies and Gentlemen!")

def bid_function(bid_participants):
    print("\n" * 10)
    print(logo.logo)
    bid_amount = 0
    while True:
        bidder_name = input("What is your name ? ")
        if len(bidder_name) == 0 or bidder_name.isspace() or '\t' in bidder_name:
            print("Sorry, you must enter your name. Please try again.")
            continue
        else:
            break

    while True:
        try:
            bid_amount = int(input("What's your bid? $ "))
        except ValueError:
            print("Sorry, invalid bid. Please try again.")
            continue
        else:
            break

    bid_participants[bidder_name] = bid_amount

    clear_console()


bidding_participants = {}
more_bids = True

while more_bids:
    bid_function(bidding_participants)

    anyone_else = (input("Are there any other bidders? type ('yes' or 'no') OR 'enter' to continue: ")).lower()
    if anyone_else == 'no':
        more_bids = False
else:
    highest_bid = 0
    winner = ""
    for name, bid in bidding_participants.items():
        if highest_bid < bid:
            highest_bid = bid
            winner = name

    print(f"Winner of this secret auction is {winner} with a bid of ${highest_bid}")

print(bidding_participants)