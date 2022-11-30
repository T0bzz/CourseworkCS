#Imports necessary files
from config import *

class Mode:
    def __init__(self, game, engine, number, screen, display_surface):
        self.game = game
        self.engine = engine
        self.number = number
        self.screen = screen
        self.display_surface = display_surface

    def event_handler(self, event):
        pass

    #Calls the update and draw subroutines
    def standard(self):
        self.update()
        self.draw()

    def update(self):
        pass

    def draw(self):
        pass

