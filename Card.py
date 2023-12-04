class Card():
    def __init__(self, card_value, card_symbol, card_image, card_back):
        self.__card_value = card_value
        self.__card_symbol = card_symbol
        self.__card_image = card_image 
        self.__card_location = ()
        self.__card_back = card_back 

    def set_card_value(self, value):
        self.__card_value = value 

    def get_card_value(self):
        return self.__card_value
    
    def get_card_symbol(self):
        return self.__card_symbol 

    def get_card_image(self):
        return self.__card_image

    def set_card_location(self, location):
        self.__card_location = location 

    def get_card_location(self):
        return self.__card_location  
    
    def get_card_back(self):
        return self.__card_back 
    
    def copy(self):
        new_card = self.__class__(self.__card_value, self.__card_symbol, self.__card_image, self.__card_back)
        return new_card 

if __name__ == '__main__':
    c = Card(10, 'A', 'image', 'cardback')  
    c.copy()
