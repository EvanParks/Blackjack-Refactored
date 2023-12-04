import pygame

class MakeButton():
    def __init__(self, xpos, ypos, image):
        self.x_pos = xpos 
        self.y_pos = ypos 
        self.__image = image
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (xpos,ypos)
        self.__buttonClicked = False
        
    def is_clicked(self):
        pressed = False

        mousePosition = pygame.mouse.get_pos()

        if self.__rect.collidepoint(mousePosition):
            if pygame.mouse.get_pressed()[0] == 1 and self.__buttonClicked == False:
                self.__buttonClicked = True
                pressed = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.__buttonClicked = False

        return pressed
    
    def draw(self, surface):
        surface.blit(self.__image, (self.__rect.x, self.__rect.y))

    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos 

if __name__ == '__main__':
    b = MakeButton(10, 10, 'image') 