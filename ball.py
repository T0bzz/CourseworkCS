import pygame
from config import *
from enum import Enum


class Colours(Enum):
    YELLOW = 1
    RED = 2
    BLACK = 3


class Ball:
    def __init__(self, x, y):
        self.colour = Colours.YELLOW
        self.velocity = pygame.math.Vector2(0,0)
        
        
    def draw(self):
        pass