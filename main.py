import cProfile
import pygame
from game import Game
from config import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.Surface((DS_WIDTH, DS_HEIGHT))

pygame.init()

def main(pr=None):
    game = Game(pr)
    running = True
    game.start(screen, display_surface)
    while running:
        game.update()


if __name__ == '_main_':
    if debug == True:
        with cProfile.Profile() as pr:
            main(pr)
    else:
        main()
