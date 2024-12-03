import random
import day11_deck_cards

card_values = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "11": 10,
    "12": 10,
    "13": 10
}

# Black Jack Game
def buy_chips(players_dict):
    for player in players_dict:
        players_dict[player].append(500) # hardcoding 1000 for now, can add logic to ask player to buy as well

def place_first_wager(players_dict):
    for player in players_dict:
        while True:
            try:
                input_wager = int(input(f"{player}, enter your wager: "))

                if players_dict[player][0] < 100:
                    players_dict[player][1] = players_dict[player][0]
                    print("Ypu are All in now.")
                    break

                if input_wager > players_dict[player][0]:
                    print("Wager is too high. Please enter a lower amount.")
                    continue
                elif input_wager < 100:
                    print("Wager is too low. Min wager is $100.")
                    continue
                else:
                    players_dict[player].append(input_wager)
                    # remaining balance
                    players_dict[player][0] -= input_wager
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return players_dict

def dealer_deal(player_dict, deck):
    dealer_hand = []
    # draw cards
    for i in range(0, 2):
        dealer_hand.append(draw_card(deck))
        for player in player_dict:
            player_dict[player].append(draw_card(deck))

    return player_dict, dealer_hand


def draw_card(deck):
    suit = random.choice(list(deck.keys()))
    card = random.choice(deck[suit])

    deck[suit].remove(card)

    return card

def get_card_value(card):
    card = str(card)
    print(type(card))
    card_value = card_values[card]
    return card_value

def setup_table():
    # setup deck
    deck = {
        "CLUBS": [card for card in range(1, 14)],
        "DIAMONDS": [card for card in range(1, 14)],
        "HEARTS": [card for card in range(1, 14)],
        "SPADES": [card for card in range(1, 14)]
    }

    number_of_players = 0
    while True:
        try:
            number_of_players = int(input("How many players are playing? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    players_dict = {}
    for num in range (1, number_of_players + 1):
        player_name = "player_" + str(num)
        players_dict[player_name] = [] # list is [chips, wager, card1, card2]

    buy_chips(players_dict)

    return players_dict, deck

def display_hands(players_dict, dealer_hand):
    card1 = dealer_hand[0]
    card2 = dealer_hand[1]
    print(f"Dealer's hand: {get_card_face(card1-1)}  |  {get_card_face(card2-1)}")
    print(40 * "_")

    for player in players_dict:
        card1 = get_card_face(players_dict[player][2]-1)
        card2 = get_card_face(players_dict[player][3]-1)
        print(f"{player}'s hand: {card1}  |  {card2}")


def get_card_face(card):
    return day11_deck_cards.CARDS[card]

def check_first_time_black_jack(dealer_hand, players_dict):

    dealer_value = 0
    for card in dealer_hand:
        dealer_value += get_card_value(card)
        # print("dealer value", dealer_value)


    for player in players_dict:
        player_value = 0
        card1_value1 = get_card_value(players_dict[player][2])
        card1_value2 = get_card_value(players_dict[player][3])
        player_value = card1_value1 + card1_value2

        if player_value == 21:
            if dealer_value == 21:
                print(f"{player} has BlackJack and draws. Dealer has BlackJack too.")
                players_dict[player].append("BLACKJACK")
            else:
                print(f"{player} has BlackJack and wins.")
                players_dict[player].append("BLACKJACK")
                players_dict[player][1] += players_dict[player][1] * 1.5

def main():
    while True:
        response = input("Do you want to play BlackJack? (Y/N) ").strip().lower()
        if response == 'y':
            play_blackjack = True
            break
        elif response == 'n':
            play_blackjack = False
            print("okieeee, bye bye!")
            return # end process
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

    players_dict, deck = setup_table() # NUMBER OF PLAYERS ON TABLE AND THEIR CHIPS
    # print(deck)
    # print(players_dict)

    players_dict = place_first_wager(players_dict) # players place wager
    # print(players_dict)

    players_dict, dealer_hand = dealer_deal(players_dict, deck) # get hands for dealer and players
    print(players_dict, dealer_hand)
    print(deck)

    display_hands(players_dict, dealer_hand)

    check_first_time_black_jack(dealer_hand, players_dict)

    while True:
        break

if __name__ == '__main__':
    main()