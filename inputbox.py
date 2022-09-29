import pygame
from math import sin, cos, tanh


class Inputbox:
    def __init__(self, eq="y = x", x=0, y=0):
        self.eq = eq
        self.x = x
        self.y = y

    def input_handler(self, event):
        if event.type == pygame.TEXTINPUT:
            if event.text in "0123456789 +-/*x().sintaco":
                self.eq += event.text
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                if len(self.eq) >= 5:
                    self.eq = self.eq[:-1]


