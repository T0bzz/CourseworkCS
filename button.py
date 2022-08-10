#Import rectangles from pygame
from pygame import Rect

#Create a button class
class Button:

    def __init__(self, x, y, primary_image, secondary_image):
        self.rect = Rect(x, y, primary_image.get_width(), primary_image.get_height())
        self.current_image = primary_image
        self.primary_image = primary_image
        self.secondary_image = secondary_image
    
    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.current_image = self.secondary_image
        else:
            self.current_image = self.primary_image

    