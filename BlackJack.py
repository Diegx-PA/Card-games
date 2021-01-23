import random

#Create a Dictionary of all the Values, suits and ranks of the cards
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
         'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self,suit,rank):
        #Creates a card with an imput
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        #returns the description of a card
        return self.rank + " of " + self.suit


class Deck:
    
    def __init__(self):
        
        self.all_cards = [] #all the cards in a deck
        
        for suit in suits: #instantiates every single suit
            for rank in ranks: #instantiates every single rank
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name, balance=0):
        
        self.name = name
        self.balance = balance
        self.all_cards = []
        self.BetPlaced = False
        self.value = 0
        self.aces =0

    def add_cards(self,new_cards):

        self.all_cards.append(new_cards)
        self.value += values[new_cards.rank]
        if new_cards.rank == 'Ace':
            self.aces += 1

    def FIX_ACES(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    def add_balance(self, amount):

        self.balance += amount
        print(f'{amount} chips have been added to your balance')

    def stakes(self,amount):

        if amount > self.balance:
            print('Sorry you dont have the funds for that')
        else:
            self.balance -= amount
            print(f'{amount} chips have been removed from your balance')
            self.BetPlaced = True
            return amount



    def __str__(self):

        return f'{self.name} has a total of: {self.balance} chips '

class Dealer:

    def __init__(self):
        self.all_cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,new_cards):

        self.all_cards.append(new_cards)
        self.value += values[new_cards.rank]
        if new_cards.rank == 'Ace':
            self.aces += 1

    def FIX_ACES(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.all_cards[1])
    print("\nPlayer's Hand:", *player.all_cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.all_cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.all_cards, sep='\n ')
    print("Player's Hand =", player.value)



def hit_or_stand():
    global playing


    while True:
        a = input("Do you want another card Y / N  ")
        if a[0].lower() == "y":
            Gamer.add_cards((new_deck.deal_one()))
        elif a[0].lower() == "n":
            playing = False
        else:
            print("Sorry i don't understand your answer. (Y / N)  ")
            continue
        break

def make_the_bet():  # I want to fucking die

    Choice = 'WRONG'
    while Choice.isdigit() == False or Gamer.BetPlaced == False:
        Choice = input('Place a bet:    ')
        if Choice.isdigit() == False:
            print('Sorry that is not a valid number')
        if Choice.isdigit() == True:
            bet = int(Choice)
            return Gamer.stakes(bet)

def hit( deck, hand):

    hand.add_cards(deck.deal_one())
    hand.FIX_ACES()

def welcome():
    print('\n' + '\t' + 'Welcome to blackjack')
    print('\n' + '\t' + 'To win your cards have to get a sum value the closest to 21')
    print('\n' + '\t' + 'The dealer will also try to get his cards the closest to 21')
    print('\n' + '\t' + 'any Ace cards will be both used as a value of 1 or 11 depending on the situation')
    print('\n' + '\t' + 'have fun')

welcome()
playing = True
GameActive = True
Gamer = Player(input("Insert your name:"))
Gamer.add_balance(500)
while GameActive == True:


    new_deck = Deck()
    new_deck.shuffle()
    new_deck.shuffle()
    new_deck.shuffle()

    new_dealer = Dealer()
    new_dealer.add_cards(new_deck.deal_one())
    new_dealer.add_cards(new_deck.deal_one())


    Gamer.add_cards(new_deck.deal_one())
    Gamer.add_cards(new_deck.deal_one())

    bet = make_the_bet()


    def player_busts():
        # GameActive = False
        print(f'{Gamer.name} busts with a value of {Gamer.value} and loses his bet of{bet} chips')

        Gamer.BetPlaced = False


    def dealer_wins():
        # GameActive = False
        print(f'The dealer wins against {Gamer.name}. {Gamer.name} loses his bet of {bet} chips ')
        Gamer.BetPlaced = False


    def dealer_busts():
        # GameActive = False
        print(f'The dealer busted, {Gamer.name} wins and doubles his bet of {bet} chips')
        Gamer.add_balance(bet * 2)
        Gamer.BetPlaced = False


    def player_wins():
        # GameActive = False
        print(f'{Gamer.name} wins against the dealer and doubles his bet of {bet} chips')
        Gamer.add_balance(bet * 2)
        Gamer.BetPlaced = False


    def push():
        # GameActive = False
        print(f'The dealer and {Gamer.name} tie, no one wins')
        Gamer.add_balance(bet)
        Gamer.BetPlaced = False

    show_some(Gamer, new_dealer)

    while playing:

        hit_or_stand()
        show_some(Gamer, new_dealer)

        if Gamer.value > 21:
            player_busts()
            break

    if Gamer.value <= 21:

        while new_dealer.value <= 17:
            hit(new_deck, new_dealer)

        show_all(Gamer, new_dealer)

        if new_dealer.value > 21:
            dealer_busts()

        elif new_dealer.value > Gamer.value:
            dealer_wins()

        elif Gamer.value > new_dealer.value:
            player_wins()

        elif Gamer.value == new_dealer.value:
            push()

    print(Gamer)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        Gamer.all_cards.clear()
        Gamer.value = 0
        new_dealer.value = 0
        new_dealer.all_cards.clear()
        new_deck = Deck()
        print(f'You have a total of {Gamer.value} chips')
        continue
    else:
        print("Thanks for playing!")
        break