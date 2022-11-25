#Imports needed libraries and files
import pygame
from mode import Mode
from config import *
from math import cos, radians
from table import Table
from pocket import Pocket
from ball import Cueball

#Creates Freeplay class
class Freeplay:
    def __init__(self, game, engine, mode, screen, display_surface, settings):
        self.game = game
        self.engine = engine
        self.mode = mode
        self.screen = screen
        self.display_surface = display_surface
        #Creates a variable for the settings class which is defined before. This method is used so the settings class does not have to be re-ran and avoiding overwritting the variables
        self.settings = settings
        #Creates a variable for and runs the Table class with necessary parameters passed in
        self.table = Table(self.game, self.engine, self.screen, self.display_surface, 0, 0, self.mode, self.settings)

        #Calls the function input_handler from the table class with event passed is as a parameter
    def input_handler(self, event):
        self.table.input_handler(event)

        #Calls the update and draw functions (Draw calls draw in freeplay). This also restarts the game when the black ball is potted
    def standard(self):
        self.table.update()
        self.draw()
        if self.table.Game_Over() == True:
            print("Restart -----------------------------------------------------------------------")
            self.game.restart()

            #Calls draw in Table, as well as drawing the main background aand scaling
    def draw(self):
        self.display_surface.fill(BLUE)
        self.table.draw()
        pygame.transform.scale(self.display_surface,
                               (WIDTH, HEIGHT), dest_surface=self.screen)
        pygame.display.flip()