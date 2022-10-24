import pygame
from config import *
from pocket import CPocket, MPocket
from cushion import Cushion
from ball import Cueball, Red_Ball, Yellow_Ball, Black_Ball
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
        self.redballs = [Red_Ball(RED1, 1, 0.5, 1), Red_Ball(RED2, 1, 0.5, 1), Red_Ball(RED3, 1, 0.5, 1), Red_Ball(RED4, 1, 0.5, 1), Red_Ball(RED5, 1, 0.5, 1), Red_Ball(RED6, 1, 0.5, 1), Red_Ball(RED7, 1, 0.5, 1)]
        self.yellowballs = [Yellow_Ball(Yellow1, 1, 0.5, 1), Yellow_Ball(Yellow2, 1, 0.5, 1), Yellow_Ball(Yellow3, 1, 0.5, 1), Yellow_Ball(Yellow4, 1, 0.5, 1), Yellow_Ball(Yellow5, 1, 0.5, 1), Yellow_Ball(Yellow6, 1, 0.5, 1), Yellow_Ball(Yellow7, 1, 0.5, 1)]
        self.blackball = Black_Ball(Black1, 1, 0.5, 1)
        self.c_pockets = [CPocket(CP_TL), CPocket(CP_TR), CPocket(CP_BL), CPocket(CP_BR)]
        self.m_pockets = [MPocket(MP_T), MPocket(MP_B)]


        self.space.add(self.cueball.body, self.cueball.shape)
        self.space.add(self.blackball.body, self.blackball.shape)
        for cushion in self.cushions:
            self.space.add(cushion.body, cushion.shape)
        for redball in self.redballs:
            self.space.add(redball.body, redball.shape)
        for yellowball in self.yellowballs:
            self.space.add(yellowball.body, yellowball.shape)
        for pocket in self.c_pockets:
            self.space.add(pocket.body, pocket.shape)
        for pocket in self.m_pockets:
            self.space.add(pocket.body, pocket.shape)

        self.input_box = Inputbox()

    def input_handler(self, event):
        self.input_box.input_handler(event)

    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(
            self.cueball.image, (int(self.cueball.body.position.x), int(self.cueball.body.position.y)))
        self.display_surface.blit(
            self.blackball.image, (int(self.blackball.body.position.x), int(self.blackball.body.position.y)))
        for redball in self.redballs:
            self.display_surface.blit(redball.image, (int(redball.body.position.x), int(redball.body.position.y)))
        for yellowball in self.yellowballs:
            self.display_surface.blit(yellowball.image, (int(yellowball.body.position.x), int(yellowball.body.position.y)))
        text = INPUT_FONT.render(
            self.input_box.eq, True, pygame.Color("turquoise"))
        self.display_surface.blit(text, text.get_rect())

    def update(self):
        self.cueball.speed_down()
        self.cueball.slow_down()
        self.blackball.speed_down()
        self.blackball.slow_down()
        for redball in self.redballs:
            redball.speed_down()
            redball.slow_down()
        for yellowball in self.yellowballs:
            yellowball.speed_down()
            yellowball.slow_down()
        print("Cueball:", self.cueball.body.velocity)
        self.space.step(1)
        # self.cueball.move(self.input_box.eq)
