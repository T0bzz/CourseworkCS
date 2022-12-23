#Imports libraries needed for functions to run the game as well as for debugging
#Files imported to run classes and store classes as variables so they only need to be ran once
import pstats
from config import *
from engine import Engine
import pygame
from mainmenu import MainMenu
from settings import Settings


#Class is used to control the game mode, initially run main menu, store classes as variables which can be passed around, and resstart the progra in certain situations
class Game:
    def __init__(self, pr, screen, display_surface):
        self.pr = pr
        self.current_mode_num = 0
        self.current_mode = None
        self.engine = Engine()
        self.screen = screen
        self.display_surface = display_surface
        self.mainmenu = MainMenu(self, self.screen, self.display_surface, self.engine, Settings(self, self.screen, self.display_surface))
    
    #Starts the program though displayinng the main menu
    def start(self):
        self.current_mode = self.mainmenu
        
    #This subroutine ubdates continuously, setting the title of the window to the current framerate, runs the standard procedure in game and update in the engine class
    def update(self):
        self.engine.update()
        pygame.display.set_caption(
            "{:.2f}".format(self.engine.clock.get_fps()))
        self.events()
        if self.current_mode is not None:
            self.current_mode.standard()

    #This subroutine runs current_mode.input_handler, and records inputs 
    def events(self):
        for event in pygame.event.get():
            self.current_mode.input_handler(event)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if debug:
                    stats = pstats.Stats(self.pr)
                    stats.sort_stats(pstats.SortKey.TIME)
                    stats.dump_stats(filename="DEBUG_FILENAME.prof")

                pygame.quit()
                exit(0)
    #This function is used to re-run the main menu in certain conditions, for example when the black ball is potted
    #def restart(self):
    #    self.current_mode = self.mainmenu