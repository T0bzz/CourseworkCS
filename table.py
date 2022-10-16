import pygame
from config import *
from pocket import Pocket
from cushion import Cushion
from ball import Cueball, Red_Ball
from ball import Cueball
from inputbox import Inputbox
import pymunk


class Table:
    def __init__(self, engine, display_surface, x, y):
        self.x = x
        self.y = y
        self.cushions = [Cushion(CUSHION1), Cushion(CUSHION2), Cushion(
            CUSHION3), Cushion(CUSHION4), Cushion(CUSHION5), Cushion(CUSHION6)]
        self.space = pymunk.Space()
        self.engine = engine
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - CUEBALL_RADIUS * 2, 209 - CUEBALL_RADIUS * 2, 1, 0.5, 9)
        self.redball = Red_Ball(RED1, 1, 0.5, 1)
        
        self.space.add(self.redball.body, self.redball.shape)
        self.space.add(self.cueball.body, self.cueball.shape)
        for cushion in self.cushions:
            self.space.add(cushion.body, cushion.shape)

        self.input_box = Inputbox()

    def input_handler(self, event):
        self.input_box.input_handler(event)

    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(
            self.cueball.image, (int(self.cueball.body.position.x), int(self.cueball.body.position.y)))
        self.display_surface.blit(self.redball.image, (int(self.redball.body.position.x), int(self.redball.body.position.y)))
        text = INPUT_FONT.render(
            self.input_box.eq, True, pygame.Color("turquoise"))
        self.display_surface.blit(text, text.get_rect())

    def update(self):
        self.cueball.speed_down()
        self.cueball.slow_down()
        self.redball.speed_down()
        self.redball.slow_down()
        print("Cueball:", self.cueball.body.velocity)
        print("Red ball: ", self.redball.body.velocity)
        self.space.step(1)
        # self.cueball.move(self.input_box.eq)
