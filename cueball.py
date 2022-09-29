import pygame
from config import *

class Cueball:
    def __init__(self, x, y, text = " "):
        self.x = x
        self.y = y
        self.velocity = pygame.math.Vector2(0,0)
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))

    def move(self, pos, eq):
        temp_pos = (self.x, self.y)
        self.x = pos[0] + 1
        try:
            self.y = eval(eq[3:])# Skips 'y ='
            if type(self.y) not in (int, float):
                raise Exception("Unexpected eval() return")
        except:
            self.x, self.y = temp_pos# Dont move is equation is invalid
        