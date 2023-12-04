from Entity import Player, Dealer  
from Deck import Deck 
from Bet import Bet 
from abc import ABC, abstractmethod 

class Blackjack_interface(ABC):
    @abstractmethod
    def get_player(self):
        pass 

    @abstractmethod
    def get_dealer(self):
        pass 

    @abstractmethod
    def get_bet(self):
        pass 

    @abstractmethod
    def get_hand_over(self):
        pass 

    @abstractmethod
    def get_player_win(self):
        pass 

    @abstractmethod
    def get_dealer_win(self):
        pass 

    @abstractmethod
    def get_bust(self):
        pass 

    @abstractmethod
    def get_draw(self):
        pass 

class Blackjack_screen(Blackjack_interface):
    def __init__(self, blackjack_instance):
        self.player = blackjack_instance.get_player()
        self.dealer = blackjack_instance.get_dealer()
        self.bet = blackjack_instance.get_bet()
        self.hand_over = blackjack_instance.get_hand_over()
        self.player_win = blackjack_instance.get_player_win()
        self.dealer_win = blackjack_instance.get_dealer_win()
        self.bust = blackjack_instance.get_bust()
        self.draw = blackjack_instance.get_draw() 
        self.blackjack_instance = blackjack_instance

    def update(self):
        self.player = self.blackjack_instance.get_player()
        self.dealer = self.blackjack_instance.get_dealer()
        self.bet = self.blackjack_instance.get_bet()
        self.hand_over = self.blackjack_instance.get_hand_over()
        self.player_win = self.blackjack_instance.get_player_win()
        self.dealer_win = self.blackjack_instance.get_dealer_win()
        self.bust = self.blackjack_instance.get_bust()
        self.draw = self.blackjack_instance.get_draw()

    def get_player(self):
        self.update()
        return self.player

    def get_dealer(self):
        self.update()
        return self.dealer

    def get_bet(self):
        self.update()
        return self.bet

    def get_hand_over(self):
        self.update()
        return self.hand_over

    def get_player_win(self):
        self.update()
        return self.player_win

    def get_dealer_win(self):
        self.update()
        return self.dealer_win

    def get_bust(self):
        self.update()
        return self.bust

    def get_draw(self):
        self.update()
        return self.draw

class Blackjack(Blackjack_interface):
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer() 
        self.deck = Deck()  
        self.bet = Bet()
        
        self.start = True
        self.paused = False
        self.playAgain = False
        self.placed_bet = False  
        self.double_down = False 
        
        self.hand_over = False
        self.game_over = False 
        self.player_win = False 
        self.dealer_win = False 
        self.draw = False
        self.bust = False 
        
    def get_player(self):
        return self.player 
    
    def get_dealer(self):
        return self.dealer 
    
    def get_deck(self):
        return self.deck 
    
    def get_bet(self):
        return self.bet 
    
    def set_start(self, boolean):
        self.start = boolean 

    def get_start(self):
        return self.start

    def set_hand_over(self, boolean):
        self.hand_over = boolean 

    def get_hand_over(self):
        return self.hand_over 
    
    def set_game_over(self, boolean):
        self.game_over = boolean 
    
    def get_game_over(self):
        return self.game_over
    
    def set_player_win(self, boolean):
        self.player_win = boolean
    
    def get_player_win(self):
        return self.player_win 
    
    def set_dealer_win(self, boolean):
        self.dealer_win = boolean 
    
    def get_dealer_win(self):
        return self.dealer_win 
    
    def set_draw(self, boolean):
        self.draw = boolean
    
    def get_draw(self):
        return self.draw 
    
    def set_bust(self, boolean):
        self.bust = boolean
    
    def get_bust(self):
        return self.bust 
    
    def set_paused(self, boolean):
        self.paused = boolean

    def get_paused(self):
        return self.paused

    def set_play_again(self, boolean):
        self.__playAgain = boolean

    def get_play_again(self):
        return self.__playAgain
    
    def set_placed_bet(self, boolean):
        self.placed_bet = boolean 
    
    def get_placed_bet(self):
        return self.placed_bet 
    
    def set_double_down(self, boolean):
        self.double_down = boolean 

    def get_double_down(self):
        return self.double_down
    
    def draw_card(self, entity):
        card = self.deck.draw_card()
        entity.add_card(card)
    
    def start_game(self):
        for i in range(2):
            self.draw_card(self.get_player())

        for i in range(2):
            self.draw_card(self.get_dealer())
        
    def check_dealer_stay(self):
        if self.dealer.calculate_card_total() >= 17:
            self.dealer.set_stay(True) 
        if self.dealer.calculate_card_total() < 17:
            self.dealer.set_stay(False)

    def check_aces(self, entity):
        aces = self.__check_aces_to_fix(entity.get_hand())

        while (entity.calculate_card_total() > 21) and (aces != []):
            ace_card = aces.pop()
            entity.get_hand()[ace_card].set_card_value(1)

    def __check_aces_to_fix(self, hand):
        aces_locations = []
        for i in range(len(hand)):
            if hand[i].get_card_symbol() == 'A' and hand[i].get_card_value() == 11:  
                aces_locations.append(i)

        return aces_locations 
    
    def apply_double_down(self):
        double_down_value = self.bet.calculate_chip_total() * 2

        if self.get_player().calculate_chip_total() + self.bet.calculate_chip_total() >= double_down_value and self.get_player().calculate_card_total() in [9, 10, 11]:
            self.bet.return_chips(self.get_player(), self.get_player_win())
            self.bet.apply_double_down_chips(self.get_player(), double_down_value)
            self.set_double_down(True) 

    def check_win(self):
        if self.player.calculate_card_total() > 21 and self.dealer.calculate_card_total() < 21:
            self.set_dealer_win(True)
            self.set_hand_over(True)
        elif self.player.calculate_card_total() < 21 and self.dealer.calculate_card_total() > 21:
            self.set_player_win(True)
            self.set_hand_over(True)
        elif self.player.calculate_card_total() == 21 and self.dealer.calculate_card_total() != 21:
            self.set_player_win(True)
            self.set_hand_over(True)
        elif self.player.calculate_card_total() != 21 and self.dealer.calculate_card_total() == 21:
            self.set_dealer_win(True)
            self.set_hand_over(True)
        elif self.player.calculate_card_total() == 21 and self.dealer.calculate_card_total() == 21:
            self.set_draw(True)
            self.set_hand_over(True)
        elif self.player.calculate_card_total() > 21 and self.dealer.calculate_card_total() > 21:
            self.set_bust(True)
            self.set_hand_over(True)
        elif self.player.get_stay() and self.dealer.get_stay(): 
            if self.player.calculate_card_total() > self.dealer.calculate_card_total():
                self.set_player_win(True)
                self.set_hand_over(True)
            elif self.player.calculate_card_total() < self.dealer.calculate_card_total():
                self.set_dealer_win(True)
                self.set_hand_over(True)
            elif self.player.calculate_card_total() < 21 and self.dealer.calculate_card_total() < 21 and self.player.calculate_card_total() == self.dealer.calculate_card_total():
                self.set_draw(True)
                self.set_hand_over(True)

        self.bet.set_bet_amount(self.bet.calculate_chip_total())

        if self.get_player_win() or self.get_bust() or self.get_draw():
            self.bet.return_chips(self.get_player(), self.get_player_win())

        self.bet.adjust_chips(self.get_player())
        self.check_amounts()
        
        if self.game_over:
            self.set_hand_over(False)

    def check_amounts(self):
        if self.get_player().calculate_chip_total() <= 0:
            self.set_dealer_win(True)
            self.set_game_over(True)
        elif self.get_player().calculate_chip_total() >= self.get_dealer().get_limit():
            self.set_player_win(True)
            self.set_game_over(True)

    def reset_game(self):
        self.deck.set_play_deck()
        self.player.clear()
        self.dealer.clear()
        self.set_hand_over(False)
        self.set_paused(False)
        self.set_player_win(False)
        self.set_dealer_win(False)
        self.set_draw(False)
        self.set_bust(False)
        self.set_play_again(False)
        self.bet.reset_chips()
        self.set_double_down(False)

        if self.get_game_over():
            self.player.reset_chips() 
            self.set_game_over(False) 
        
if __name__ == '__main__':
    b = Blackjack()


    
    
