import pygame
from config import *
from pocket import Pocket
from cushion import Cushion
from cueball import Cueball
from inputbox import Inputbox
import pymunk


class Table:
    def __init__(self, engine, display_surface, x, y):
        self.x = x
        self.y = y
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.space.fricton = 100
        self.engine = engine
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - CUEBALL_RADIUS * 2,
                               209 - CUEBALL_RADIUS * 2, 1, 0.5)

        self.space.add(self.cueball.body, self.cueball.shape)
        self.input_box = Inputbox()

    def input_handler(self, event):
        self.input_box.input_handler(event)

    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        print(self.cueball.body.position)
        self.display_surface.blit(
            self.cueball.image, (int(self.cueball.body.position.x), int(self.cueball.body.position.y)))
        text = INPUT_FONT.render(
            self.input_box.eq, True, pygame.Color("turquoise"))
        self.display_surface.blit(text, text.get_rect())

    def update(self):
        self.cueball.body.apply_impulse_at_local_point((5, 0))
        self.space.step(self.engine.dt)
        #self.cueball.move(self.input_box.eq)
