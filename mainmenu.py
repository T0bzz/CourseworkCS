#import libraries and classes needed for the program
import pygame
import math
import sys
from config import *
from button import Button
from freeplay import Freeplay
from mode import Mode
from level import Level
from settings import Settings


class MainMenu:
    def __init__(self, game, screen, display_surface, engine, settings):
        self.game = game
        self.screen = screen
        self.display_surface = display_surface
        self.engine = engine
        self.settings = settings

        #Gets the folders and files needed to draw the images
        #Class B Files organised for sequential access
        folders = os.listdir(BUTTONS_FOLDER)
        for folder in folders:
            BUTTONS[folder] = (pygame.image.load(path.join(BUTTONS_FOLDER, folder, "primary.png")).convert_alpha(
            ), pygame.image.load(path.join(BUTTONS_FOLDER, folder, "secondary.png")).convert_alpha())

        #Stores the folder of images needed in an array
        self.buttons = []
        self.buttons.append(Button(690, 250, BUTTONS["Title"]))
        self.buttons.append(
            Button(885, 400, BUTTONS["Freeplay"], self.start_freeplay))
        self.buttons.append(Button(885, 550, BUTTONS["Levels"], self.start_level))
        self.buttons.append(Button(885, 700, BUTTONS["Settings_Main"], self.start_settings))

    def input_handler(self, event):
        return

    #Calls the update and draw subroutines
    def standard(self):
        self.update()
        self.draw()

    #Gets the mouse position 
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update(mouse_pos)

    #Draws the background and images on the screen. The images will change if the user's cursor is hovering over the image
    def draw(self):
        self.screen.fill(WHITE)
        for button in self.buttons:
            self.screen.blit(
                button.current_image, (button.rect.x, button.rect.y))
        
    
    #Sets the current mode in the game class as freeplay, and passes in necessary parameters
    def start_freeplay(self):
        self.game.current_mode = Freeplay(
            self.game, self.engine, -1, self.screen, self.display_surface, self.settings)

    #Sets the current mode in the game class as level, and passes in necessary parameters
    def start_level(self):
        level_balls = []
        for i in range(6):
            level_red_pos = (random.randint(167, 549), random.randint(112, 290))
            level_balls.append(level_red_pos)
        self.game.current_mode = Level(self.game, self.engine, 1, self.screen, self.display_surface, self.settings, level_balls)

    #Sets the current mode in the game class as settings, and passes in necessary parameters
    def start_settings(self):
        self.game.current_mode = self.settings