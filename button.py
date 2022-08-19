#Import rectangles from pygame
from pygame import Rect, Surface, mask, mouse
from config import SF


#Create a button class
class Button:

    def __init__(self, x, y, images: tuple[Surface, Surface], function=None):
        self.primary_image, self.secondary_image = images
        self.current_image = self.primary_image
        self.rect = Rect(x, y, self.primary_image.get_width(), self.primary_image.get_height())
        self.mask = mask.from_surface(self.primary_image)
        self.function = function
    
    def update(self, mouse_pos):
        mouse_pos_in_mask = mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y
        if self.rect.collidepoint(mouse_pos) and self.mask.get_at(mouse_pos_in_mask):
            self.current_image = self.secondary_image
            if self.function is not None:
                if mouse.get_pressed()[0]:
                    self.function()
        else:
            self.current_image = self.primary_image

    