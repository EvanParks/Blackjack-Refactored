from Button import MakeButton
from LoadImages import LoadImages 

class Buttons():
    def __init__(self):
        self.__all_images = LoadImages() 
        self.start_button = MakeButton(round(self.__all_images.get_screen_width() / 2.4), round(self.__all_images.get_screen_height() / 1.8), self.__all_images.get_start_image()) #897 500
        self.exit_button = MakeButton(round(self.__all_images.get_screen_width() / 1.9), round(self.__all_images.get_screen_height() / 1.8), self.__all_images.get_exit_image()) #897 600
        self.pause_button = MakeButton(round(self.__all_images.get_screen_width() / 192), round(self.__all_images.get_screen_height() / 108), self.__all_images.get_pause_image()) #10 10
        self.hit_button = MakeButton(round(self.__all_images.get_screen_width() / 1.1), round(self.__all_images.get_screen_height() / 1.8), self.__all_images.get_hit_image()) #1780 600
        self.stay_button = MakeButton(round(self.__all_images.get_screen_width() / 1.1), round(self.__all_images.get_screen_height() / 1.5), self.__all_images.get_stay_image()) #1780 700
        self.double_down_button = MakeButton(round(self.__all_images.get_screen_width() / 1.1), round(self.__all_images.get_screen_height() / 2.25), self.__all_images.get_double_down_image()) 
        self.cont_button = MakeButton(round(self.__all_images.get_screen_width() / 2.1), round(self.__all_images.get_screen_height() / 2.1), self.__all_images.get_cont_image()) #897 500
        self.leave_button = MakeButton(round(self.__all_images.get_screen_width() / 2.1), round(self.__all_images.get_screen_height() / 1.8), self.__all_images.get_leave_image()) #897 600
        self.play_again_button = MakeButton(round(self.__all_images.get_screen_width() / 2.4), round(self.__all_images.get_screen_height() / 2.2), self.__all_images.get_play_again_image()) #800 600
        self.next_hand_button = MakeButton(round(self.__all_images.get_screen_width() / 2.4), round(self.__all_images.get_screen_height() / 2.2), self.__all_images.get_next_hand_image()) #800 600
        self.quit_button = MakeButton(round(self.__all_images.get_screen_width() / 1.9), round(self.__all_images.get_screen_height() / 2.2), self.__all_images.get_quit_image()) #1000 600
        self.bet_button = MakeButton(round(self.__all_images.get_screen_width() / 2.1), round(self.__all_images.get_screen_height() / 1.8), self.__all_images.get_bet_image()) #1000 600
        self.thousand_chip_button = MakeButton(round(self.__all_images.get_screen_width() / 3.2), round(self.__all_images.get_screen_height() / 1.27), self.__all_images.get_chip_thousand()) #1000 600
        self.five_hundred_chip_button = MakeButton(round(self.__all_images.get_screen_width() / 2.56), round(self.__all_images.get_screen_height() / 1.27), self.__all_images.get_chip_five_hundred()) #1000 600
        self.one_hundred_chip_button = MakeButton(round(self.__all_images.get_screen_width() / 2.13), round(self.__all_images.get_screen_height() / 1.27), self.__all_images.get_chip_one_hundred()) #1000 600
        self.fifty_chip_button = MakeButton(round(self.__all_images.get_screen_width() / 1.829), round(self.__all_images.get_screen_height() / 1.27), self.__all_images.get_chip_fifty()) #1000 600
        self.twenty_five_chip_button = MakeButton(round(self.__all_images.get_screen_width() / 1.6), round(self.__all_images.get_screen_height() / 1.27), self.__all_images.get_chip_twenty_five()) #1000 600

    def get_start_button(self):
        return self.start_button

    def get_exit_button(self):
        return self.exit_button 

    def get_pause_button(self):
        return self.pause_button 
    
    def get_hit_button(self):
        return self.hit_button 
    
    def get_stay_button(self):
        return self.stay_button 
    
    def get_leave_button(self):
        return self.leave_button  
    
    def get_cont_button(self):
        return self.cont_button  
    
    def get_play_again_button(self):
        return self.play_again_button 
    
    def get_quit_button(self):
        return self.quit_button
    
    def get_next_hand_button(self):
        return self.next_hand_button
    
    def get_bet_button(self):
        return self.bet_button
    
    def get_double_down_button(self):
        return self.double_down_button
    
    def get_thousand_chip_button(self):
        return self.thousand_chip_button
    
    def get_five_hundred_chip_button(self):
        return self.five_hundred_chip_button
    
    def get_one_hundred_chip_button(self):
        return self.one_hundred_chip_button
    
    def get_fifty_chip_button(self):
        return self.fifty_chip_button
    
    def get_twenty_five_chip_button(self):
        return self.twenty_five_chip_button