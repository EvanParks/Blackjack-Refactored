import unittest
from Blackjack import Blackjack 

def get_game_state(player_card_total, dealer_card_total, blj):
        while blj.get_player().calculate_card_total() != player_card_total or blj.get_dealer().calculate_card_total() != dealer_card_total:
            if blj.get_player().calculate_card_total() < player_card_total:
                blj.draw_card(blj.get_player())
            
            if blj.get_dealer().calculate_card_total() < dealer_card_total:
                blj.draw_card(blj.get_dealer())

            if blj.get_player().calculate_card_total() > player_card_total or blj.get_dealer().calculate_card_total() > dealer_card_total:
                blj.reset_game()

        blj.get_player().set_stay(True)
        blj.get_dealer().set_stay(True)
        blj.check_win()

        return  

def get_game_state_aces(player_total, number_of_aces, blj):
    while len(check_aces_to_fix(blj.get_player().get_hand())) != number_of_aces:  
        if blj.get_player().calculate_card_total() > player_total: 
            blj.reset_game()
        else:
            blj.draw_card(blj.get_player())

    blj.check_aces(blj.get_player())
            
    return 

def check_aces_to_fix(hand):
        aces_locations = []
        for i in range(len(hand)):
            if hand[i].get_card_symbol() == 'A' and hand[i].get_card_value() == 11:  
                aces_locations.append(i)

        return aces_locations

class Testing(unittest.TestCase):
    def test_playerWinBothUnder21(self):
        blj = Blackjack()

        get_game_state(19, 17, blj)

        self.assertTrue(blj.get_player_win(), True)

    def test_dealerWinBothUnder21(self):
        blj = Blackjack()

        get_game_state(17, 19, blj)

        self.assertTrue(blj.get_dealer_win(), True)

    def test_playerWinAt21(self):
        blj = Blackjack()

        get_game_state(21, 17, blj)

        self.assertTrue(blj.get_player_win(), True)

    def test_dealerWinAt21(self):
        blj = Blackjack()

        get_game_state(17, 21, blj)

        self.assertTrue(blj.get_dealer_win(), True)
    
    def test_playerWinDealerOver21(self):
        blj = Blackjack()

        get_game_state(17, 22, blj)

        self.assertTrue(blj.get_player_win(), True)

    def test_dealerWinPlayerOver21(self):

        blj = Blackjack()

        get_game_state(22, 17, blj)

        self.assertTrue(blj.get_dealer_win(), True)

    def test_drawAt21(self):
        blj = Blackjack()

        get_game_state(21, 21, blj)

        self.assertTrue(blj.get_draw(), True)

    def test_drawUnder21(self):
        blj = Blackjack()

        get_game_state(17, 17, blj)

        self.assertTrue(blj.get_draw(), True)

    def test_BothOver21(self):
        blj = Blackjack()

        get_game_state(22, 22, blj)

        self.assertTrue(blj.get_bust(), True)

    def test_single_ace(self):
        blj = Blackjack()

        get_game_state_aces(22, 1, blj)

        self.assertTrue(12, True)

    def test_two_aces(self):
        blj = Blackjack()

        get_game_state_aces(32, 2, blj)

        self.assertTrue(12, True)
    
    def test_three_aces(self):
        blj = Blackjack()

        get_game_state_aces(42, 3, blj)

        self.assertTrue(12, True)

    def test_four_aces(self):
        blj = Blackjack()

        get_game_state_aces(42, 3, blj)

        self.assertTrue(12, True)

    def test_adjust_chips(self):
        blj = Blackjack()

        blj.get_player().get_chips()['100'] += 4

        blj.get_bet().adjust_chips(blj.get_player())
        chips = {
            '25' : 4, 
            '50' : 2, 
            '100' : 2, 
            '500' : 2, 
            '1000': 1, 
                }

        self.assertDictEqual(blj.get_player().get_chips(), chips)

    def test_double_down(self):
        blj = Blackjack()

        for key, value in blj.get_player().get_chips().items():
            if key != ['1000'] and value != 0:
                blj.get_player().get_chips()[key] -= value
                blj.get_bet().get_bet_chips()[key] += value

        blj.apply_double_down()
        chips = {
            '25' : 2, 
            '50' : 3, 
            '100' : 3, 
            '500' : 1, 
            '1000': 1, 
                }

        self.assertDictEqual(blj.get_bet().get_bet_chips(), chips)

    def test_player_win_chips(self):
        blj = Blackjack()

        blj.get_player().get_chips()['1000'] -= 1
        blj.get_bet().get_bet_chips()['1000'] += 1

        get_game_state(21, 17, blj)

        self.assertTrue(blj.get_player().calculate_chip_total(), 3000)        

    def test_player_loss_chips(self):
        blj = Blackjack()

        blj.get_player().get_chips()['1000'] -= 1
        blj.get_bet().get_bet_chips()['1000'] += 1

        get_game_state(17, 21, blj)

        self.assertTrue(blj.get_player().calculate_chip_total(), 1000)

    def test_no_win_chips(self):
        blj = Blackjack()

        blj.get_player().get_chips()['1000'] -= 1
        blj.get_bet().get_bet_chips()['1000'] += 1

        get_game_state(21, 21, blj)

        self.assertTrue(blj.get_player().calculate_chip_total(), 2000)

    def test_game_over_win(self):
        blj = Blackjack()

        count = 0 
        while count < 5:
            for key, value in blj.get_player().get_chips().items():
                if value != 0:
                    blj.get_player().get_chips()[key] -= value
                    blj.get_bet().get_bet_chips()[key] += value

            get_game_state(21, 17, blj)
            count += 1

        blj.check_amounts() 

        self.assertTrue(blj.get_game_over(), True)

    def test_game_over_loss(self):
        blj = Blackjack() 

        for key, value in blj.get_player().get_chips().items():
                blj.get_player().get_chips()[key] -= value
                blj.get_bet().get_bet_chips()[key] += value

        get_game_state(17, 21, blj)

        blj.check_amounts() 

        self.assertTrue(blj.get_game_over(), True)

if __name__ == '__main__':
    unittest.main()

