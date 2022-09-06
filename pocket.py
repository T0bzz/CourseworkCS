import pygame
from config import *
from ball import Ball


class Pocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_pot(self):
        balls = balls_potted[:]
        for i in range(len(balls_potted)):
            dist = ((self.x - balls_potted[i].x) **
                    2 + (self.y - balls_potted[i].y)**2)**0.5
            if dist < self.r + RADIUS:
                if balls_potted[i] in balls:
                    if balls_potted[i].ball_num == 8:
                        pass
                    else:
                        balls.remove(balls_potted[i])
