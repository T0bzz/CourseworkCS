import pygame
import pymunk
from config import *


class CPocket:
    def __init__(self, position):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Circle(self.body, POCKET_RADIUS)
        self.shape.density = 100000000000000000
        self.shape.elasticity = 0

class MPocket():
    def __init__(self, position):        
        self.x, self.y = position
        self.body = pymunk.Body()
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Circle(self.body, POCKET_RADIUS)
        self.shape.density = 100000000000000000
        self.shape.elasticity = 0