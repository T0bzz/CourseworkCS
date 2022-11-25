#Imports needed libraries
from time import perf_counter
from config import *

from pygame.time import Clock

#Creates Engine class
class Engine:
    def __init__(self):
        self.clock = Clock()
        self.t1 = perf_counter()

    #Sets prfcounter as well as FPS which would be shown at the top of the window when not in full screen, used for derbugging 
    def update(self):
        self.clock.tick(FPS)
        self.dt = (perf_counter() - self.t1)
        self.t1 = perf_counter()