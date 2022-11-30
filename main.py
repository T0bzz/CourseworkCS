#Imports files for classes needed
#Libraries are imported for useful functions needed to run the game. E.g. Debugging and pygame
import cProfile
import pygame
from game import Game
from config import *

#Variables defined using constants defined in config 
#Screen and config used to display the window, display_surface is used for scaling
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.Surface((DS_WIDTH, DS_HEIGHT))

#Initialise pygame, allowing the window to be displayed
pygame.init()

#Main funcion used to run the game through using subroutines created in the game class
def main(pr=None):
    #Runs the game class.
    #A variable is used to the game class is not re-ran everytime its needed, overiding variables.
    game = Game(pr, screen, display_surface)
    running = True
    game.start()
    while running:
        game.update()
        pygame.display.flip()

#Runs main function if the file name is main.py
if __name__ == '__main__':
    #Runs with debugging enabled if the debugging variable in config is set to true
    if debug:
        with cProfile.Profile() as pr:
            main(pr)
    #Runs without debugging if debugging is False
    else:
        main()