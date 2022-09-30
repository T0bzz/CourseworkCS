import pygame
from config import *
import pymunk


class Cueball:
    def __init__(self, x, y, mass, moment):
        self.body = pymunk.Body(mass, moment)
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, RADIUS)
        self.body.friction = 10
        self.body.velocity = pymunk.Vec2d(0, 0)
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))

    def move(self, eq):
        temp_pos = (self.x, self.y)
        self.x += 1
        try:
            self.y = eval(eq[3:])  # Skips 'y ='
            if type(self.y) not in (int, float):
                raise Exception("Unexpected eval() return")
        except:
            self.x, self.y = temp_pos  # Dont move is equation is invalid
