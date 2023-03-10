import random

deck = []
colors = ["red", "yellow", "green", "blue"]
special_cards = ["Skip", "Reverse", "Draw Two"]
wild_cards = ["Wild", "Wild Draw Four"]

for color in colors:
    for i in range(10):
        card = "{} {}".format(color, i)
        deck.append(card)
    for special in special_cards:
        card = "{} {}".format(color, special)
        deck.append(card)

for wild in wild_cards:
    for i in range(4):
        card = wild
        deck.append(card)

# Shuffle the deck
random.shuffle(deck)

# Initialize the players
num_players = int(input("Enter the number of players: "))
players = []
for i in range(num_players):
    player = {"name": "Player {}".format(i+1), "hand": []}
    players.append(player)

# Deal cards to each player
for i in range(7):
    for player in players:
        card = deck.pop()
        player["hand"].append(card)

# Initialize the discard pile
discard_pile = []
card = deck.pop()
discard_pile.append(card)

# Initialize the game state
game_over = False
current_player = 0
direction = 1

# Define a function to check if a card can be played
def can_play(card):
    top_card = discard_pile[-1]
    color, value = card.split()
    top_color, top_value = top_card.split()
    if color == "Wild" or color == top_color or value == top_value:
        return True
    return False

# Define a function to play a card
def play_card(player, card):
    player["hand"].remove(card)
    discard_pile.append(card)
    print("{} played {}".format(player["name"], card))

# Define a function to draw a card
def draw_card(player):
    card = deck.pop()
    player["hand"].append(card)
    print("{} drew a card".format(player["name"]))

# Define a function to skip a player
def skip_player():
    global current_player, num_players, direction
    current_player = (current_player + (direction * 1)) % num_players
    print("Player {} was skipped".format(current_player+1))

# Define a function to reverse the direction
def reverse_direction():
    global direction
    direction = direction * -1
    print("The direction of play has been reversed")

# Define a function to draw two cards and skip a player
def draw_two_cards():
    global current_player, num_players, direction
    for i in range(2):
        draw_card(players[(current_player + (direction * 1)) % num_players])
    skip_player()

# Define a function to draw four cards and skip a player
def draw_four_cards():
    global current_player, num_players, direction
    for i in range(4):
        draw_card(players[(current_player + (direction * 1)) % num_players])
    skip_player()

# Main game loop
while not game_over:
    player = players[current_player]
    print("Top card: {}".format(discard_pile[-1]))
    print("{}'s turn".format(player["name"]))
    print("Your hand: {}".format(player["hand"]))
    if any(can_play(card) for card in player["hand"]):
        card_index = int(input("Enter the index of the card you want to play (or -1 to draw a card): "))
        if card_index == -1:
            draw_card(player)
        else:
            card = player["hand"][card_index]