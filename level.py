import pygame
from table import Table
from config import *
from table import Table


class Level:
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

    def draw(self):
        self.display_surface.fill(BLUE)
        self.table.draw()
        pygame.transform.scale(self.display_surface,
                               (WIDTH, HEIGHT), dest_surface=self.screen)
        pygame.display.flip()