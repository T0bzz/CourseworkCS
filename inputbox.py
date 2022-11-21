import pygame
from math import sin, cos, tan


class Inputbox():
    def __init__(self):
        self.angle_input = "Angle: 180"
        self.force_input = "Force: 8000"
        self.play = False


    def update(self):
        self.play = False
        if self.input_handler_angle() == True and self.input_handler_force() == True:
            self.play = False
        return self.play

    def input_handler_angle(self, event):
        self.play = False
        if event.type == pygame.TEXTINPUT:
            if event.text in "0123456789.-":
                if len(self.angle_input) <= 12:
                    self.angle_input += event.text
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                if len(self.angle_input) >= 8:
                    self.angle_input = self.angle_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.play = True
            elif event.key == pygame.K_DOWN:
                self.input_handler_force()
                

    def input_handler_force(self, event):
        self.play = False 
        if event.type == pygame.TEXTINPUT:
            if event.text in "0123456789,-":
                if len(self.force_input) <= 12:
                    self.text_input += event.text
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                if len(self.force_input) >= 8:
                    self.force_input = self.force_input[:-1]
                elif event.key == pygame.K_RETURN:
                    self.play == True
                elif event.key == pygame.K_UP:
                    self.input_
                

