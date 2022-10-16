import pygame
from config import *


class CPocket:
    def __init__(self, position):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.body = pymunk.Circle(self.body, CP_RADIUS)

class MPocket(CPocket):
    def __init__(self, position):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.body = pymunk.Circle(self.body, MP_RADIUS)