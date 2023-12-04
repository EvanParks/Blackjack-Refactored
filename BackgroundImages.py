from LoadImages import LoadImages

class BackgroundImages():
    def __init__(self):
        self.all_images = LoadImages()
        self.background = self.all_images.get_bg() 

    def get_background_image(self):
        return self.background 
    
    
