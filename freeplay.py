import pygame
from mode import Mode
from config import *
from ball import Ball
from math import cos, radians
from table import Table
from pocket import Pocket
from cueball import Cueball
from inputbox import Input



class Freeplay(Mode):
    def __init__(self, game, engine, mode, screen, display_surface):
        self.game = game
        self.engine = engine
        self.mode = mode
        self.screen = screen
        self.display_surface = display_surface
        self.table = Table(display_surface, 0, 0)
        self.inputbox = input()
        

    def standard(self):
        self.draw()

    def draw(self):
        self.display_surface.fill(BLUE)
        self.table.draw()
        self.inputbox.Tk()
        pygame.transform.scale(self.display_surface,
                               (WIDTH, HEIGHT), dest_surface=self.screen)
        pygame.display.flip()

