from LoadImages import LoadImages

class ChipImages():
    def __init__(self):
        self.all_images = LoadImages()
        self.thousand_chip_image = self.all_images.get_chip_thousand()
        self.five_hundred_chip_image = self.all_images.get_chip_five_hundred()
        self.one_hundred_chip_image = self.all_images.get_chip_one_hundred()
        self.fifty_chip_image = self.all_images.get_chip_fifty()
        self.twenty_five_chip_image = self.all_images.get_chip_twenty_five()

    def get_chip_images(self):
        return [('1000', self.thousand_chip_image) \
                ,('500', self.five_hundred_chip_image) \
                ,('100', self.one_hundred_chip_image) \
                , ('50', self.fifty_chip_image) \
                , ('25', self.twenty_five_chip_image)]
