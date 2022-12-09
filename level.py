#Imports necessary libraries and classes which are needed for the code
import pygame
from table import Table
from config import *
from table import Table


class Level:
    def __init__(self, game, engine, mode, screen, display_surface, settings):
        self.game = game
        self.engine = engine
        self.mode = mode
        self.screen = screen
        self.display_surface = display_surface
        self.settings = settings
        self.table = Table(self.game, self.engine, self.screen, self.display_surface, 0, 0, self.mode, self.settings, 0, 0)

    #Calls the input handler from the table class
    def input_handler(self, event):
        self.table.input_handler(event)

    #Calls update in the table class and draw procedure
    def standard(self):
        self.table.update()
        self.draw()

    #Draws the background, calls draw fom the table class nd scales the image
    def draw(self):
        self.display_surface.fill(BLUE)
        self.table.draw()
        pygame.transform.scale(self.display_surface,
                               (WIDTH, HEIGHT), dest_surface=self.screen)
        