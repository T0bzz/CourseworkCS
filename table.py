import pygame
import pymunk
import math
from config import *
from pocket import Pocket
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
        self.static_body = self.space.static_body
        self.engine = engine
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2, 5, self.static_body)
        self.redball = [Red_Ball(RED1, 5, self.static_body), Red_Ball(RED2, 5, self.static_body), Red_Ball(RED3, 5, self.static_body), Red_Ball(RED4, 5, self.static_body), Red_Ball(RED5, 5, self.static_body), Red_Ball(RED6, 5, self.static_body), Red_Ball(RED7, 5, self.static_body)]
        self.yellowball = [Yellow_Ball(Yellow1, 5, self.static_body), Yellow_Ball(Yellow2, 5, self.static_body), Yellow_Ball(Yellow3, 5, self.static_body), Yellow_Ball(Yellow4, 5, self.static_body), Yellow_Ball(Yellow5, 5, self.static_body), Yellow_Ball(Yellow6, 5, self.static_body), Yellow_Ball(Yellow7, 5, self.static_body)]
        self.blackball = Black_Ball(Black1, 1, self.static_body)
        self.pockets = [Pocket(CP_TL), Pocket(CP_TR), Pocket(CP_BL), Pocket(CP_BR), Pocket(MP_T), Pocket(MP_B)]

        self.space.add(self.cueball.body, self.cueball.shape, self.cueball.pivot)
        self.space.add(self.blackball.body, self.blackball.shape, self.blackball.pivot)
        for cushion in self.cushions:
            self.space.add(cushion.body, cushion.shape)
        for redball in self.redball:
            self.space.add(redball.body, redball.shape, redball.pivot)
        for yellowball in self.yellowball:
            self.space.add(yellowball.body, yellowball.shape, yellowball.pivot)
        for pockets in self.pockets:
            self.space.add(pockets.body, pockets.shape)
        

        self.input_box = Inputbox()


    def input_handler(self, event):
        self.input_box.input_handler(event)



    def draw(self):
        pygame.draw.line(self.display_surface, WHITE, (0, 0), (50, 720), width=5)
        self.display_surface.blit(self.image, (self.x, self.y))
        self.display_surface.blit(
            self.cueball.image, ((self.cueball.body.position.x), (self.cueball.body.position.y)))
        self.display_surface.blit(
            self.blackball.image, ((self.blackball.body.position.x), (self.blackball.body.position.y)))
        for redball in self.redball:
            self.display_surface.blit(redball.image, ((redball.body.position.x), (redball.body.position.y)))
        for yellowball in self.yellowball:
            self.display_surface.blit(yellowball.image, ((yellowball.body.position.x), (yellowball.body.position.y)))
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
        for pocket in pocket_coords:
            cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
            cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
            cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
            if cue_dist < POCKET_RADIUS:
                self.display_surface.blit(self.cueball.image, (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2))
                self.cueball.body.velocity = (0, 0)

    def update(self):
        self.pocket()
        print("Cueball:", self.cueball.body.velocity)
        self.space.step(1/120)
        if self.input_box.play and self.cueball.body.velocity == (0, 0):
            self.cueball.move((self.cueball.body.position), self.input_box.eq)
        else:
            pass
        if self.input_box.play:
            self.input_box.play = False

