import pygame
from math import sin, cos, tan


class Inputbox():
    def __init__(self):
        self.angle_input = "Angle: 180"
        self.play = False

    def input_handler(self, event):
        self.play = False
        if event.type == pygame.TEXTINPUT:
            if event.type == pygame.TEXTINPUT:
                if event.text in "0123456789.-":
                    self.angle_input += event.text
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                self.angle_input = self.angle_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.play = True
                


