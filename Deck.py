from Card import Card
import random 
from LoadImages import LoadImages

class Deck():
    def __init__(self):  
        self.__images = LoadImages().get_image_deck() 
        self.__card_back = LoadImages().get_card_back() 
        self.__card_deck = self.initializeDeck() 
        self.__card_play_deck = self.set_play_deck() 
         
    def initializeDeck(self):
        values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        symbols = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        count = 0
        i = 0
        deck = []
        while i in range(len(values)-1):
            for j in range(len(self.__images)):
                if count <= 3:
                    deck.append(Card(values[i], symbols[i], self.__images[j], self.__card_back))
                    count +=1
                if count == 4:
                    i +=1
                    count = 0

        return deck 
    
    def clone_card(self, card):
        return card.copy() 
    
    def set_play_deck(self):
        self.__card_play_deck = [self.clone_card(card) for card in self.__card_deck]
        self.shuffle_play_deck(self.__card_play_deck)
        return self.__card_play_deck 
    
    def get_card_deck(self):
        return self.__card_deck 
    
    def draw_card(self):
        card = self.__card_play_deck.pop() 
        return card 

    def shuffle_play_deck(self, deck):
        for i in range(len(deck) - 1, 0, -1):
            j = random.randint(0, i)
            deck[i], deck[j] = deck[j], deck[i]

        return deck 

    def get_card_play_deck(self):
        return self.__card_play_deck 

    def get_card_back(self):
        return self.__card_back
    
if __name__ == '__main__':
    d = Deck() 
    for i in range(len(d.get_card_play_deck())):
        print(d.get_card_play_deck()[i].get_card_symbol())

   

