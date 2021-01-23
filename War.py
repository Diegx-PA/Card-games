import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
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
    def __str__(self):
        return f'{self.name}'

    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)



new_deck = Deck()
new_deck.shuffle()



player_one = Player(input("Insert Player 1 name: "))
player_two = Player(input("Insert Player 2 name: "))

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0
while game_on == True:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print(f'{player_one} has no more cards')
        print(f'{player_two} wins. THE GAME ENDS')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(f'{player_two} has no more cards')
        print(f'{player_one} wins. THE GAME ENDS')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    
    while at_war == True:
        if player_two_cards[-1].value > player_one_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print(f'{player_one} was unable to play war. Game ends at war')
                print(f'{player_two} WINS')
                game_on = False
                break
            if len(player_one.all_cards) < 5:
                print(f'{player_two} was unable to play war. Game ends at war')
                print(f'{player_one} WINS')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one)
                    player_two_cards.append(player_two.remove_one)
                    at_war = False