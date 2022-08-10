#import modules
import pygame
import math
import sys
from config import *

# Create class for menu


class MainMenu:
    def __init__(self, screen, display_surface, engine):
        self.screen = screen
        self.display_surface = display_surface
        self.engine = engine
        self.buttons = []

    def global_update(self):
        self.update()
        self.draw()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update(mouse_pos)

    def draw(self):
        self.display_surface.fill(WHITE)
        for button in self.buttons:
            self.display_surface.blit(button.current_image, (button.rect.x, button.rect.y))
        pygame.transform.scale(self.display_surface, (WIDTH, HEIGHT), dest_surface=self.screen)
        pygame.display.flip()

    