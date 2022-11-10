import pygame, math
from ball import Cueball

class Cuestick():
    def __init__(self, pos):
        self.posx, self.posy = pygame.mouse.get_pos()
        self.cueball = Cueball()
        self.angle = 0

    def rotate(self):
        ball_posx, ball_posy = self.cueball.body.position.x, self.cueball.body.position.y
        angle_x, angle_y = self.posx - ball_posx, self.posy - ball_posy
        self.angle = (180 / math.pi) * -math.atan2(angle_x, angle_y)

