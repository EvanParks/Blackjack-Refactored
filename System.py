import pygame 
from Screen import Screen 
from Blackjack import Blackjack, Blackjack_screen 

pygame.init() 
pygame.display.set_caption("BlackJack")

class System():
    def __init__(self): 
        self.blackjack = Blackjack()
        self.blackjack_screen = Blackjack_screen(self.blackjack)
        self.screen = Screen(self.blackjack_screen) 

    def get_screen(self):
        return self.screen 

    def get_blackjack(self):
        return self.blackjack
    
    def get_blackjack_screen(self):
        return self.blackjack_screen

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
    
            self.get_screen().draw_background()

            if self.blackjack.get_start():
                self.screen.draw_start_game() 
                if self.screen.get_buttons().get_start_button().is_clicked():
                    print('Start')
                    self.blackjack.set_placed_bet(True) 
                    self.blackjack.set_start(False) 
                if self.screen.get_buttons().get_exit_button().is_clicked():
                    print('Quit')
                    running = False
                    
            elif self.blackjack.get_paused():
                self.screen.draw_pause_game() 
                if self.screen.get_buttons().get_cont_button().is_clicked():
                    print('Continue')
                    self.blackjack.set_paused(False)
                if self.screen.get_buttons().get_leave_button().is_clicked():
                    print('Exit')
                    self.blackjack.set_paused(False)
                    self.blackjack.set_game_over(True) 
                    self.blackjack.reset_game()
                    self.blackjack.set_start(True)

            elif self.blackjack.get_hand_over():
                self.screen.draw_hand_over() 
                if self.screen.get_buttons().get_next_hand_button().is_clicked():
                    print('Next Hand')
                    self.blackjack.set_placed_bet(True)
                    self.blackjack.reset_game()
                    self.blackjack.set_hand_over(False)
                if self.screen.get_buttons().get_quit_button().is_clicked():
                    print('Exit')
                    self.blackjack.set_hand_over(False)
                    self.blackjack.set_game_over(True) 
                    self.blackjack.reset_game()
                    self.blackjack.set_start(True) 
                    
            elif self.blackjack.get_placed_bet(): 
                self.screen.draw_bet()
                if self.screen.get_buttons().get_thousand_chip_button().is_clicked():
                    if self.blackjack.player.get_chips()['1000'] > 0:
                        self.blackjack.player.get_chips()['1000'] -= 1
                        self.blackjack.get_bet().get_bet_chips()['1000'] += 1

                if self.screen.get_buttons().get_five_hundred_chip_button().is_clicked():
                    if self.blackjack.player.get_chips()['500'] > 0:
                        self.blackjack.player.get_chips()['500'] -= 1
                        self.blackjack.get_bet().get_bet_chips()['500'] += 1

                if self.screen.get_buttons().get_one_hundred_chip_button().is_clicked():
                    if self.blackjack.player.get_chips()['100'] > 0:
                        self.blackjack.player.get_chips()['100'] -= 1
                        self.blackjack.get_bet().get_bet_chips()['100'] += 1

                if self.screen.get_buttons().get_fifty_chip_button().is_clicked():
                    if self.blackjack.player.get_chips()['50'] > 0:
                        self.blackjack.player.get_chips()['50'] -= 1
                        self.blackjack.get_bet().get_bet_chips()['50'] += 1

                if self.screen.get_buttons().get_twenty_five_chip_button().is_clicked():
                    if self.blackjack.player.get_chips()['25'] > 0:
                        self.blackjack.player.get_chips()['25'] -= 1
                        self.blackjack.get_bet().get_bet_chips()['25'] += 1

                if self.screen.get_buttons().get_bet_button().is_clicked():
                    print('Bet')
                    if self.blackjack.get_bet().calculate_chip_total() > 0:
                        self.blackjack.start_game()
                        self.blackjack.set_placed_bet(False) 

            elif self.blackjack.get_game_over():
                self.screen.draw_game_over()
                if self.screen.get_buttons().get_play_again_button().is_clicked():
                    print('Play Again')
                    self.blackjack.set_placed_bet(True)
                    self.blackjack.reset_game()
                    self.blackjack.set_game_over(False)
                if self.screen.get_buttons().get_quit_button().is_clicked():
                    print('Exit')
                    self.blackjack.reset_game()
                    self.blackjack.set_start(True)
                    self.blackjack.set_game_over(False)

            else:
                self.screen.draw_game() 
                if self.screen.get_buttons().get_pause_button().is_clicked():
                    print('Paused')
                    self.blackjack.set_paused(True)

                if self.screen.get_buttons().get_hit_button().is_clicked() and not self.blackjack.player.get_stay() and self.blackjack.player.calculate_card_total() <= 21:
                    print('hit')
                    self.blackjack.draw_card(self.blackjack.get_player())
                    if not self.blackjack.dealer.get_stay():
                        self.blackjack.draw_card(self.blackjack.get_dealer())

                if self.screen.get_buttons().get_stay_button().is_clicked():
                    print('stay')
                    self.blackjack.player.set_stay(True)
                    while not self.blackjack.dealer.get_stay():
                        self.blackjack.draw_card(self.blackjack.get_dealer())
                        self.blackjack.check_aces(self.blackjack.dealer)
                        self.blackjack.check_dealer_stay()

                if self.screen.get_buttons().get_double_down_button().is_clicked():
                    print('Double Down')
                    if not self.blackjack.get_double_down():
                        self.blackjack.apply_double_down()

                self.blackjack.check_aces(self.blackjack.player)
                
                if self.blackjack.player.get_stay() and self.blackjack.dealer.get_stay():
                    self.blackjack.check_win() 

            pygame.display.update()
            
        pygame.quit() 

if __name__ == '__main__':
    s = System() 
    s.run_game() 