import random
from time import sleep
from os import system
import sys

# Creating and shuffling(Fisher-Yates) deck of cards:

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        if val == 11:
            self.value = "Jack"
        if val == 12:
            self.value = "Queen"
        if val == 13:
            self.value = "King"
        if val == 1:
            self.value = "Ace"

    def show(self):
        print(f'{self.value} of {self.suit}')



class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['Clubs', 'Hearts', 'Clubs', 'Diamonds']:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()



class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

# Interactive function to play the game:


dealer = Player("Dealer")
deck = Deck()
deck.shuffle()

def play():
    player_count = 0
    dealer_count = 0
    player1.draw(deck)
    player1.show_hand()
    sleep(0.9)
    dealer.draw(deck)
    dealer.show_hand()
    player1.draw(deck)
    player1.show_hand()
    faketype("Would you like to hit or stand?")
    y = input("(h/s) ")
    if y.lower() == 'h':
        player1.draw(deck)
        player1.show_hand()

    while player_count < 21:
        pass


# Function to clear terminal:

def clear():
    name = 'nt'
    if name == 'nt':
        _ = system('cls')

# Function to make it look like a human is typing in the terminal:

words = " "
def faketype(words):
  words
  for char in words:
    sleep(random.choice([0.2, 0.3, 0.04, 0.03, 0.04, 0.04, 0.03, 0.03, 0.04, 0.01]))
    sys.stdout.write(char)
    sys.stdout.flush()
  sleep(1)


# First Page:

print("""
####   #        #     ###   #   #  #####    #     ###   #   #
#   #  #       # #   #   #  #  #      #    # #   #   #  #  #
####   #      #   #  #      # #       #   #   #  #      # #
#   #  #      #####  #      ###       #   #####  #      ###
#   #  #      #   #  #   #  #  #   #  #   #   #  #   #  #  #
####   #####  #   #   ###   #   #   ##    #   #   ###   #   #
-------------------------------------------------------------
Welcome to BlackJack
-------------------------------------------------------------
""")
  
print("Let's get started...")
input("(Click Enter to Continue)")
sleep(0.5)
clear()

# Second page:

faketype("What's your name?")
player1 = Player(input(" "))

faketype(f"Nice to meet you {player1.name}. ")
faketype("Are you familiar with the rules of blackjack? ")
x = input("(y/n) ")
if x.lower() == 'n':
    faketype("That's ok, I can teach you. ")
    sleep(2)
    clear()
    faketype(f"""
Okay {player1.name}, Here are the rules: You and the dealer both start with 2 cards. To win the game, the sum of your 
cards has to be closer to 21 than the sum of the dealers cards. You can to try your chances by drawing a card, and adding
it to the total of your hand. If you go over 21, you instantly lose. Sounds pretty easy right? Yeah... but theres
a catch. You can only see one of the dealers cards until the end of the game. If the dealer has less than 17, then
they draw another card. 
""")
    sleep(1)
    faketype("Understand? ")
    if input("(y/n)") == 'y':
        pass
    else:
        faketype("Well you're a lost cause then, idiot.")
elif x.lower() == 'y':
    faketype("Alrighty then, I'll grab the deck of cards! ")
else:
    faketype("Sorry, I didn't catch that, please try again. ")

deck.show()


