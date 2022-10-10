import pygame
import pymunk
from config import *



class Ball:
    def __init__(self, x, y, mass=1, moment=0.5):
        self.image_redball = pygame.image.load(path.join(BALL_FOLDER, "Redball.png"))
        self.image_yellowball = pygame.image.load(path.join(BALL_FOLDER, "Yellowball.png"))
        self.image_balckball = pygame.image.load(path.join(BALL_FOLDER, "Blackball.png"))
        self.body = pymunk.Body(mass, moment)
        self.shape = pymunk.Circle(self.body, CUEBALL_RADIUS)
        self.shape.elasticity = 1
        
