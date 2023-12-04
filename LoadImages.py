import pygame

pygame.init() 
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("BlackJack")

class LoadImages():     
    def __init__(self): 
        self.screen_info = pygame.display.Info() 
        self.screen_width = self.screen_info.current_w
        self.screen_height = self.screen_info.current_h
        self.bg = pygame.image.load("Images\\backgroundImage.png").convert_alpha()
        self.card_back = self.load_and_scale_image("Images\\red_back.png", (round(self.screen_width / 12.8), round(self.screen_height / 5.4))) 
        self.pause_image = self.load_and_scale_image("Images\\pauseImage.png", (round(self.screen_width / 42.6), round(self.screen_height / 24)))
        self.start_image = self.load_and_scale_image("Images\\startImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.exit_image = self.load_and_scale_image("Images\\exitImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.hit_image = self.load_and_scale_image("Images\\hitImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.stay_image = self.load_and_scale_image("Images\\standImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.leave_image = self.load_and_scale_image("Images\\leaveImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.cont_image = self.load_and_scale_image("Images\\resumeImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.play_again_image = self.load_and_scale_image("Images\\restartImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.next_hand_image = self.load_and_scale_image("Images\\nextHandImage.png", (round(self.screen_width / 16), round(self.screen_height / 18))) 
        self.quit_image = self.load_and_scale_image("Images\\quitImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.bet_image = self.load_and_scale_image("Images\\betImage2.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.double_down_image = self.load_and_scale_image("Images\\doubleDownImage.png", (round(self.screen_width / 16), round(self.screen_height / 18)))
        self.chip_thousand = self.load_and_scale_image("Images\\Chip_Thousand.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha()  
        self.chip_five_hundred = self.load_and_scale_image("Images\\Chip_Five_Hundred.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha()
        self.chip_one_hundred = self.load_and_scale_image("Images\\Chip_One_Hundred.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha() 
        self.chip_fifty = self.load_and_scale_image("Images\\Chip_Fifty.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha()
        self.chip_twenty_five = self.load_and_scale_image("Images\\Chip_Twenty_Five.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha()
        self.chip_ten = self.load_and_scale_image("Images\\Chip_Ten.png", (round(self.screen_width / 12.8), round(self.screen_height / 7.2))).convert_alpha() 
        self.image_deck = self.card_deck_images() 
      
    def load_and_scale_image(self, image_path, size):
        image = pygame.image.load(image_path).convert_alpha()

        return pygame.transform.smoothscale(image, size)
    
    def card_deck_images(self):
        directory = []
        actualDeck = []
        for i in range(1,14):
            for j in range(1,5):
                directory.append("Images\\" + str(i) + "_" + str(j) + ".png")
        for card in directory:
            actualDeck.append(pygame.transform.smoothscale(pygame.image.load(card), (round(self.screen_width / 12.8), round(self.screen_height / 5.4))))
    
        return actualDeck 
    
    def get_bg(self):
        return self.bg 
    
    def get_card_back(self):
        return self.card_back
    
    def get_image_deck(self):
        return self.image_deck 

    def get_start_image(self):
        return self.start_image

    def get_exit_image(self):
        return self.exit_image
    
    def get_pause_image(self):
        return self.pause_image 

    def get_hit_image(self):
        return self.hit_image 
    
    def get_stay_image(self):
        return self.stay_image 
    
    def get_leave_image(self):
        return self.leave_image 
    
    def get_cont_image(self):
        return self.cont_image 
    
    def get_play_again_image(self):
        return self.play_again_image 
    
    def get_bet_image(self):
        return self.bet_image
    
    def get_quit_image(self):
        return self.quit_image
    
    def get_double_down_image(self):
        return self.double_down_image
    
    def get_next_hand_image(self):
        return self.next_hand_image

    def get_chip_thousand(self):
        return self.chip_thousand 
    
    def get_chip_five_hundred(self):
        return self.chip_five_hundred
    
    def get_chip_one_hundred(self):
        return self.chip_one_hundred
    
    def get_chip_fifty(self):
        return self.chip_fifty
    
    def get_chip_twenty_five(self):
        return self.chip_twenty_five
    
    def get_chip_ten(self):
        return self.chip_ten 
    
    def get_screen_width(self):
        return self.screen_width
    
    def get_screen_height(self):
        return self.screen_height 
    
if __name__ == '__main__':
    LI = LoadImages()
    print(LI.get_screen_height())
    print(LI.get_screen_width()) 

