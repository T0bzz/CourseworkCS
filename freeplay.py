import pygame
from mode import Mode
from config import *
from math import cos, radians
from table import Table
from pocket import Pocket
from ball import Cueball


class Freeplay:
    def __init__(self, game, engine, mode, screen, display_surface):
        self.game = game
        self.engine = engine
        self.mode = mode
        self.screen = screen
        self.display_surface = display_surface
        self.table = Table(self.game, self.engine, self.screen, self.display_surface, 0, 0, self.mode)

    def input_handler(self, event):
        self.table.input_handler(event)

    def standard(self):
        self.table.update()
        self.draw()
        if self.table.Game_Over() == True:
            print("Restart -----------------------------------------------------------------------")
            self.game.restart()

    def draw(self):
        self.display_surface.fill(BLUE)
        self.table.draw()
        pygame.transform.scale(self.display_surface,
                               (WIDTH, HEIGHT), dest_surface=self.screen)
        pygame.display.flip()