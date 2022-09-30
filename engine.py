from time import perf_counter
from config import *

from pygame.time import Clock


class Engine:
    def __init__(self):
        self.clock = Clock()
        self.t1 = perf_counter()

    def update(self):
        self.clock.tick(FPS)
        self.dt = (perf_counter() - self.t1)
        self.t1 = perf_counter()