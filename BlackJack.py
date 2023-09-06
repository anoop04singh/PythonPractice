#BlackJack Games

import random
#First we create all the cards.
suit = ["Hearts","Clubs","Spades","Diamonds"]
rank = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
#Then we define classes based and determined on the basis of the game logic

class Cards: #Class Card Defines the cards with nessarry functions.
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank+" of "+self.suit

  class Deck():#creates a deck and has functions like shuffle and Deal
    
    def __init__(self):
        self.allCards = []
        for i in suit:
            for j in rank:
                self.allCards.append(Cards(i,j))
                
    def shuffle(self):
        random.shuffle(self.allCards)
    def dealOne(self):
        return self.allCards.pop()

    class Player():#stores player names and cards they have. It has fuunctions to remove and add cards.
    
    def __init__(self,name):
        self.name = name
        self.allCards =[]
    def removeOne(self):
        return self.allCards.pop(0)
    
    def addOne(self,newcards):
        if type(newcards) == type([]):
            self.allCards.extend(newcards)
        else:
            self.allCards.append(newcards)
    
    def __str__(self):
        return "Player {} has {} cards.".format(self.name,len(self.allCards))

    #GAME SETUP

player1 = Player("Anoop") #defining players
player2 = Player("Gurnash")

newDeck = Deck()
newDeck.shuffle() #creating and shuffling deck.

for x in range(26): #dealing cards to the players
    player1.addOne(newDeck.dealOne())
    player2.addOne(newDeck.dealOne())

##Game Logic
gameOn = True
rCount = 0 #round COUNTER
while gameOn:
    rCount += 1
    print("The Round is {}".format(rCount))
    
    if len(player1.allCards) == 0: #CHECKS IF THE PLAYER HAAS CARDS OR NOT
        print("Player {} out of Cards".format(player1.name))
        print("Player {} Won!!".format(player2.name))
        gameOn = False
        break
        
    if len(player2.allCards) == 0:
        print("Player {} out of Cards".format(player2.name))
        print("Player {} Won!!".format(player1.name))
        gameOn = False
        break
        
    player1Cards = [] #stores the card played by the respective player(cards that are played on the table from plaeyrs hand.)
    player1Cards.append(player1.removeOne())
    player2Cards = []
    player2Cards.append(player2.removeOne())
    
    atWar = True
    
    while atWar:
        
        if player1Cards[-1].value > player2Cards[-1].value: #once played compares the card
            player1.addOne(player1Cards)
            player1.addOne(player2Cards)
            atWar = False
            
        elif player1Cards[-1].value < player2Cards[-1].value:
            player2.addOne(player2Cards)
            player2.addOne(player1Cards)
            atWar = False
        
        else: #if the values are equal it declares a war
            print("WAR")
            
            if len(player1.allCards) < 5: #if player has less cards than that required for war
                print("Player {} out of cards".format(player1.name))
                print("Player {} Wins!".format(player2.name))
                gameOn = False
                break
                
                
            elif len(player2.allCards) < 5:
                print("Player {} out of cards".format(player2.name))
                print("Player {} Wins!".format(player1.name))
                gameOn = False
                break
            
            for i in range(5): #deal cards for the player's hand to the table and continues.
                player1Cards.append(player1.removeOne())
                player2Cards.append(player2.removeOne())
