import cProfile
import pygame
from game import Game
from config import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.Surface((DS_WIDTH, DS_HEIGHT))

pygame.init()


def main(pr=None):
    game = Game(pr, screen, display_surface)
    running = True
    game.start()
    while running:
        game.update()


if __name__ == '__main__':
    if debug == True:
        with cProfile.Profile() as pr:
            main(pr)
    else:
        main()
