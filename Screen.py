import pygame
from Buttons import Buttons
from BackgroundImages import BackgroundImages
from ChipImages import ChipImages

pygame.init() 
pygame.display.set_caption("BlackJack")

class Screen():
    def __init__(self, blackjack_screen):
        self.blackjack_screen = blackjack_screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.buttons = Buttons() 
        self.background_images = BackgroundImages()
        self.chip_images = ChipImages()
        self.black = (0, 0, 0)
        self.screen_info = pygame.display.Info() 
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h
        self.x_locations = self.set_x_locations() 
        self.chip_buttons = [('1000', self.buttons.get_thousand_chip_button()) \
                            ,('500', self.buttons.get_five_hundred_chip_button()) \
                            ,('100', self.buttons.get_one_hundred_chip_button()) \
                            ,('50', self.buttons.get_fifty_chip_button())   
                            ,('25', self.buttons.get_twenty_five_chip_button())] 

    def get_screen(self):
        return self.screen 
    
    def get_buttons(self):
        return self.buttons 
    
    def get_background(self):
        return self.background_images

    def get_chip_images(self):
        return self.chip_images 
    
    def get_screen_width(self):
        return self.screen_width
    
    def get_screen_height(self):
        return self.screen_height 
    
    def draw_background(self):
        self.screen.blit(self.background_images.get_background_image(), (0,0))

    def draw_start_game(self):
        self.buttons.get_start_button().draw(self.screen)
        self.buttons.get_exit_button().draw(self.screen)
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 5.4)).render("Blackjack", 1, self.black), (round(self.get_screen_width() / 3), round(self.get_screen_height() / 3.6)))

    def draw_pause_game(self):
        self.buttons.get_cont_button().draw(self.screen)
        self.buttons.get_leave_button().draw(self.screen)
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 5.4)).render("Paused", 1, self.black), (round(self.get_screen_width() / 2.7), round(self.get_screen_height() / 3.6))) #690 300 

    def draw_game(self):
        self.draw_hand(self.blackjack_screen.get_player(), self.blackjack_screen.get_hand_over())
        self.draw_hand(self.blackjack_screen.get_dealer(), self.blackjack_screen.get_hand_over())

        self.draw_chip_images(self.blackjack_screen.get_player().get_chips(), True)
        self.draw_chip_images(self.blackjack_screen.get_bet().get_bet_chips(), False)
        
        self.buttons.get_pause_button().draw(self.screen)
        self.buttons.get_hit_button().draw(self.screen)
        self.buttons.get_stay_button().draw(self.screen)
        self.buttons.get_double_down_button().draw(self.screen)

        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Card Total: " + str(self.blackjack_screen.get_player().calculate_card_total()), 1, self.black), (round(self.get_screen_width() / 2.3), round(self.get_screen_height() / 1.33))) #843 750
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Chips: " + "{:,}".format((self.blackjack_screen.get_player().calculate_chip_total())), 1, self.black), (round(self.get_screen_width() / 1.2), round(self.get_screen_height() / 1.05))) #1700 1025
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Limit: " + "{:,}".format((self.blackjack_screen.get_dealer().get_limit())), 1, self.black), (round(self.get_screen_width() / 1.2), round(self.get_screen_height() / 108))) #1700 10

    def draw_hand_over(self):
        self.draw_hand(self.blackjack_screen.get_player(), self.blackjack_screen.get_hand_over())
        self.draw_hand(self.blackjack_screen.get_dealer(), self.blackjack_screen.get_hand_over())

        self.draw_chip_images(self.blackjack_screen.get_player().get_chips(), True)

        self.buttons.get_quit_button().draw(self.screen)
        self.buttons.get_next_hand_button().draw(self.screen) 

        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 10.8)).render("Hand Over", 1, self.black), (round(self.get_screen_width() / 2.5), round(self.get_screen_height() / 3))) #768 400
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Card Total: " + str(self.blackjack_screen.get_dealer().calculate_card_total()), 1, self.black), (round(self.get_screen_width() / 2.3), round(self.get_screen_height() / 3.6))) #843 300
        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Card Total: " + str(self.blackjack_screen.get_player().calculate_card_total()), 1, self.black), (round(self.get_screen_width() / 2.3), round(self.get_screen_height() / 1.33))) #843 750

        if self.blackjack_screen.get_player_win():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("You Win $" + str(self.blackjack_screen.get_bet().get_bet_amount()), 1, self.black), (round(self.get_screen_width() / 2.2), round(self.get_screen_height() / 2.5)))  #902 500
            
        elif self.blackjack_screen.get_draw():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("It's a Draw", 1, self.black), (round(self.get_screen_width() / 2.15), round(self.get_screen_height() / 2.5)))  #890 500

        elif self.blackjack_screen.get_bust():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("You Both Bust", 1, self.black), (round(self.get_screen_width() / 2.2), round(self.get_screen_height() / 2.5)))  #860 500
        
        elif not self.blackjack_screen.get_player_win() and not self.blackjack_screen.get_draw() and not self.blackjack_screen.get_bust():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("You Lose $" + str(self.blackjack_screen.get_bet().get_bet_amount()), 1, self.black), (round(self.get_screen_width() / 2.2), round(self.get_screen_height() / 2.5)))  #897 500

    def draw_bet(self):
            self.draw_chip_buttons(self.blackjack_screen.get_player()) 
            self.draw_chip_images(self.blackjack_screen.get_bet().get_bet_chips(), False)
            
            self.buttons.get_bet_button().draw(self.screen)
            
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 10.8)).render("Place an Amount to Bet", 1, self.black), (round(self.get_screen_width() /  3.3), round(self.get_screen_height() / 4))) #768 400
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Chips: " + "{:,}".format((self.blackjack_screen.get_player().calculate_chip_total())), 1, self.black), (round(self.get_screen_width() / 1.2), round(self.get_screen_height() / 1.05))) #1700 1025
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 21.6)).render("Limit: " + "{:,}".format((self.blackjack_screen.get_dealer().get_limit())), 1, self.black), (round(self.get_screen_width() / 1.2), round(self.get_screen_height() / 108))) #1700 10
          
    def draw_game_over(self):
        self.buttons.get_quit_button().draw(self.screen)
        self.buttons.get_play_again_button().draw(self.screen) 

        self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 10.8)).render("Game Over", 1, self.black), (round(self.get_screen_width() / 2.5), round(self.get_screen_height() / 3.6))) #768 400

        if self.blackjack_screen.get_player_win():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("You Win", 1, self.black), (round(self.get_screen_width() / 2.13), round(self.get_screen_height() / 2.5)))  #902 500
            
        elif self.blackjack_screen.get_dealer_win():
            self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render("You Lose", 1, self.black), (round(self.get_screen_width() / 2.14), round(self.get_screen_height() / 2.5)))  #897 500

    def set_x_locations(self):
        x_locations = []
        sign = 1 
        x_location = round(self.screen_width / 2.4)
        count = 1 

        while count < 11:
            x_locations.append(x_location)
            x_location += (sign * count * round(self.screen_width / 12.8))
            sign *= -1
            count += 1

        return x_locations 

    def draw_hand(self, entity, hand_over):
        one_card = False 

        for i in range(len(entity.get_hand())):
            if entity.get_is_dealer():
                if not one_card and not hand_over:
                    self.screen.blit(entity.get_hand()[i].get_card_back(), (self.x_locations[i], round(self.screen_height / 13.5)))
                    one_card = True 
                else:
                    self.screen.blit(entity.get_hand()[i].get_card_image(), (self.x_locations[i], round(self.screen_height / 13.5)))
            else:
                self.screen.blit(entity.get_hand()[i].get_card_image(), (self.x_locations[i], round(self.screen_height / 1.8)))

    def draw_chip_buttons(self, player):
        for i in range(len(self.chip_buttons)):
            if player.get_chips()[self.chip_buttons[i][0]] > 0:
                self.chip_buttons[i][1].draw(self.screen)
                self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render(str(player.get_chips()[self.chip_buttons[i][0]]), 1, self.black),(self.chip_buttons[i][1].get_x_pos() + round(self.screen_width / 28.2), self.chip_buttons[i][1].get_y_pos() + round(self.screen_height / 6.75)))
    
    def draw_chip_images(self, chips, is_player_chips):
        x_locations = [round(self.screen_width / 3.2), round(self.screen_width / 2.56), round(self.screen_width / 2.13), round(self.screen_width / 1.829), round(self.screen_width / 1.6)]
        if is_player_chips:
            y_location = round(self.screen_height / 1.27)
        else:
            y_location = round(self.screen_height / 3.09) 

        for i in range(len(self.chip_images.get_chip_images())):
            if chips[self.chip_images.get_chip_images()[i][0]] > 0:
                self.screen.blit(self.chip_images.get_chip_images()[i][1], (x_locations[i], y_location))
                self.screen.blit(pygame.font.SysFont("Serpentine", round(self.get_screen_height() / 27)).render(str(chips[self.chip_images.get_chip_images()[i][0]]), 1, self.black),(x_locations[i] + round(self.screen_width / 28.2), y_location + round(self.screen_height / 6.75)))

if __name__ == '__main__':
    screen = Screen() 
    print(screen.x_locations) 

