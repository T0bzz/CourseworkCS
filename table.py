import pygame
import pymunk
import math
from config import *
from pocket import CPocket, MPocket
from cushion import Cushion
from ball import Cueball, Red_Ball, Yellow_Ball, Black_Ball
from ball import Cueball
from inputbox import Inputbox



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
        self.cueball = Cueball(260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2, 1, 0.5, 9)
        self.redball = [Red_Ball(RED1, 1, 0.5, 1), Red_Ball(RED2, 1, 0.5, 1), Red_Ball(RED3, 1, 0.5, 1), Red_Ball(RED4, 1, 0.5, 1), Red_Ball(RED5, 1, 0.5, 1), Red_Ball(RED6, 1, 0.5, 1), Red_Ball(RED7, 1, 0.5, 1)]
        self.yellowball = [Yellow_Ball(Yellow1, 1, 0.5, 1), Yellow_Ball(Yellow2, 1, 0.5, 1), Yellow_Ball(Yellow3, 1, 0.5, 1), Yellow_Ball(Yellow4, 1, 0.5, 1), Yellow_Ball(Yellow5, 1, 0.5, 1), Yellow_Ball(Yellow6, 1, 0.5, 1), Yellow_Ball(Yellow7, 1, 0.5, 1)]
        self.blackball = Black_Ball(Black1, 1, 0.5, 1)
        self.c_pockets = [CPocket(CP_TL), CPocket(CP_TR), CPocket(CP_BL), CPocket(CP_BR)]
        self.m_pockets = [MPocket(CP_TL), MPocket(CP_TR)]

        self.space.add(self.cueball.body, self.cueball.shape)
        self.space.add(self.blackball.body, self.blackball.shape)
        for cushion in self.cushions:
            self.space.add(cushion.body, cushion.shape)
        for redball in self.redball:
            self.space.add(redball.body, redball.shape)
        for yellowball in self.yellowball:
            self.space.add(yellowball.body, yellowball.shape)
        for pockets in self.c_pockets:
            self.space.add(pockets.body, pockets.shape)
        for pockets in self.m_pockets:
            self.space.add(pockets.body, pockets.shape)

        self.input_box = Inputbox()


    def input_handler(self, event):
        self.input_box.input_handler(event)



    def draw(self):
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(
            self.cueball.image, (int(self.cueball.body.position.x), int(self.cueball.body.position.y)))
        self.display_surface.blit(
            self.blackball.image, (int(self.blackball.body.position.x), int(self.blackball.body.position.y)))
        for redball in self.redball:
            self.display_surface.blit(redball.image, (int(redball.body.position.x), int(redball.body.position.y)))
        for yellowball in self.yellowball:
            self.display_surface.blit(yellowball.image, (int(yellowball.body.position.x), int(yellowball.body.position.y)))
        text = INPUT_FONT.render(
            self.input_box.eq, True, pygame.Color("turquoise"))
        self.display_surface.blit(text, text.get_rect())

    def pocket(self):
        #Red and yellow balls
        for pocket in pocket_coords:
            for ball in self.redball:
                #print(pocket_coords)
                #print(ball.body.position.x)
                red_x_dist = abs((ball.body.position.x) - (pocket[0]))
                red_y_dist = abs((ball.body.position.y) - (pocket[1]))
                red_dist = math.sqrt((red_x_dist**2) + (red_y_dist**2))
                if red_dist < POCKET_RADIUS:
                    self.space.remove(ball.body, ball.shape)
                    self.redball.remove(ball)
                    self.display_surface.blit(ball.image, (0, 0))
        for pocket in pocket_coords:
            for ball in self.yellowball:
                yellow_x_dist = abs((ball.body.position.x) - (pocket[0]))
                yellow_y_dist = abs((ball.body.position.y) - (pocket[1]))
                yellow_dist = math.sqrt((yellow_x_dist**2) + (yellow_y_dist**2))
                if yellow_dist < POCKET_RADIUS:
                    self.space.remove(ball.body, ball.shape)
                    self.display_surface.blit(ball.image, (0, 0))

    def update(self):
        self.pocket()
        for redball in self.redball:
            redball.speed_down()
            redball.slow_down()
        for yellowball in self.yellowball:
            yellowball.speed_down()
            yellowball.slow_down()
        #pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
        #pivot.max_bias = 0
        #pivot.max_force = 10
        print("Cueball:", self.cueball.body.velocity)
        self.space.step(1)
        # self.cueball.move(self.input_box.eq)

