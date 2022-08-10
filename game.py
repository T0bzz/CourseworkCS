import pstats
from config import *
from engine import Engine
import pygame
from mainmenu import MainMenu


class Game:

    def __init__(self, pr, screen, display_surface):
        self.pr = pr
        self.current_mode_num = 0
        self.current_mode = None
        self.engine = Engine()
        self.screen = self.screen
        self.display_surface = self.display_surface
    
    def start(self):
        print("Start")
        self.current_mode = MainMenu(self.screen, self.display_surface)
        

    def update(self):
        pygame.display.set_caption(
            "{:.2f}".format(self.engine.clock.get_fps()))
        if self.current_mode is not None:
            print("if")
            self.current_mode.global_update()

    def events(self):
        for event in pygame.get_event():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if debug:
                    stats = pstats.Stats(self.pr)
                    stats.sort_stats(pstats.SortKey.TIME)
                    stats.dump_stats(filename="DEBUG_FILENAME")

                pygame.quit()
                exit(0)

    

