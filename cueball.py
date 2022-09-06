import pygame
from config import *

class Cueball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = pygame.math.Vector2(0,0)
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))