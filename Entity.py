class Entity():
    def __init__(self):
        self.__hand = []
        self.stay = False 
        self.is_dealer = False 
    
    def set_stay(self, boolean):
        self.stay = boolean 

    def get_stay(self):
        return self.stay  

    def get_hand(self):
        return self.__hand
    
    def get_is_dealer(self):
        return self.is_dealer
    
    def add_card(self, card): 
        self.__hand.append(card)
    
    def calculate_card_total(self):
        total = 0 
        for i in range(len(self.__hand)):
            total += int(self.__hand[i].get_card_value()) 

        return total 
    
    def clear(self):
        self.__hand = [] 
        self.stay = False 

class Player(Entity):
    def __init__(self):
        super().__init__() 
        self.is_dealer = False 
        self.chips = {
            '25' : 2, 
            '50' : 3, 
            '100' : 3, 
            '500' : 1, 
            '1000': 1, 
                }

    def reset_chips(self):
        self.chips = {
            '25' : 2, 
            '50' : 3, 
            '100' : 3, 
            '500' : 1, 
            '1000': 1, 
                }

    def get_chips(self):
        return self.chips 
    
    def calculate_chip_total(self):
        total = 0
        for key, value in self.chips.items():
            total += int(key) * value 

        return total 

class Dealer(Entity):
    def __init__(self):
        super().__init__() 
        self.is_dealer = True 
        self.limit = 10000 

    def get_limit(self):
        return self.limit  

 

