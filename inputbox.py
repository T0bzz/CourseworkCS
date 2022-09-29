import pygame
from math import sin, cos, tanh


class Inputbox:
    def __init__(self, eq="y = x", x=0, y=0):
        self.eq = eq
        self.x = x
        self.y = y 

    def input(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.TEXTINPUT:
                    if event.text in "0123456789 +-/*x().sintaco":
                        eq += event.text
                elif event.type == pygame.KEYUP:
                    if event.text == pygame.BACKSPACE:
                        eq = eq[:-1]
                    elif event.text == pygame.ESCAPE:
                        self.x, self.y = 0,0
        