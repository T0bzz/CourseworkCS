#Imports libraries needed to record inuts form the user
import pygame


class Inputbox():
    def __init__(self):
        self.angle_input = "Angle: 180"
        self.play = False

    #This subroutine is used to record the inputs from the user for the angle input. The result will be displayed in a rect object in table
    def input_handler_angle(self, event):
        self.play = False
        if event.type == pygame.TEXTINPUT:
            #Limits the valid inpouts from the user to improve security
            if event.text in "0123456789.-":
                if len(self.angle_input) <= 9:
                    self.angle_input += event.text
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                if len(self.angle_input) >= 8:
                    self.angle_input = self.angle_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.play = True
                

