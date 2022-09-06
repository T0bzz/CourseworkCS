import pygame
from config import *
from pocket import Pocket
from cushion import Cushion
from cueball import Cueball

class Table():
    def __init__(self,display_surface, x, y):
        self.x = x
        self.y = y
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - CUEBALL_RADIUS * 2, 209 - CUEBALL_RADIUS * 2)
        

    def update(self):
        pass

    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(self.cueball.image, (self.cueball.x, self.cueball.y))
        