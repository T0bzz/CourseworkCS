import pygame
import pymunk
import math
from math import cos, sin, tan, radians
from config import *
from pocket import Pocket
from cushion import Cushion
from ball import Cueball, Red_Ball, Yellow_Ball, Black_Ball
from ball import Cueball
from inputbox import Inputbox



class Table:
    def __init__(self, engine, display_surface, x, y, mode):
        self.x = x
        self.y = y
        self.red_increment = 0
        self.yellow_increment = 0
        self.red_balls_potted = 0
        self.yellow_balls_potted = 0
        self.mode = mode
        self.coords_potted = [0, 30, 60, 90, 120, 150, 180]
        self.force = FORCE 
        self.max_force = MAX_FORCE
        self.direction = DIRECTION
        self.cushions = [Cushion(CUSHION1), Cushion(CUSHION2), Cushion(
            CUSHION3), Cushion(CUSHION4), Cushion(CUSHION5), Cushion(CUSHION6), Cushion(S_CP_TL_1), Cushion(S_CP_TL_2), Cushion(S_MP_T_1), Cushion(S_MP_T_2), Cushion(S_CP_TR_1), Cushion(S_CP_TR_2), Cushion(S_CP_BR_1), Cushion(S_CP_BR_2), Cushion(S_MP_B_1), Cushion(S_MP_B_2), Cushion(S_CP_BL_1), Cushion(S_CP_BL_2)]
        self.space = pymunk.Space()
        self.static_body = self.space.static_body
        self.engine = engine
        self.display_surface = display_surface
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2, 5, self.static_body)
        if self.mode == -1:
            self.redball = [Red_Ball(RED1, 5, self.static_body), Red_Ball(RED2, 5, self.static_body), Red_Ball(RED3, 5, self.static_body), Red_Ball(RED4, 5, self.static_body), Red_Ball(RED5, 5, self.static_body), Red_Ball(RED6, 5, self.static_body), Red_Ball(RED7, 5, self.static_body)]
            self.yellowball = [Yellow_Ball(Yellow1, 5, self.static_body), Yellow_Ball(Yellow2, 5, self.static_body), Yellow_Ball(Yellow3, 5, self.static_body), Yellow_Ball(Yellow4, 5, self.static_body), Yellow_Ball(Yellow5, 5, self.static_body), Yellow_Ball(Yellow6, 5, self.static_body), Yellow_Ball(Yellow7, 5, self.static_body)]
            self.blackball = Black_Ball(Black1, 5, self.static_body)
        elif self.mode == 1:
            self.redball = [Red_Ball(L_RED1, 5, self.static_body), Red_Ball(L_RED2, 5, self.static_body), Red_Ball(L_RED3, 5, self.static_body), Red_Ball(L_RED4, 5, self.static_body), Red_Ball(L_RED5, 5, self.static_body), Red_Ball(L_RED6, 5, self.static_body)]
        self.pockets = [Pocket(CP_TL), Pocket(CP_TR), Pocket(CP_BL), Pocket(CP_BR), Pocket(MP_T), Pocket(MP_B)]



        
        for cushion in self.cushions:
                self.space.add(cushion.body, cushion.shape)
        if self.mode == -1:
            self.space.add(self.cueball.body, self.cueball.shape, self.cueball.pivot)
            self.space.add(self.blackball.body, self.blackball.shape, self.blackball.pivot)
            for redball in self.redball:
                self.space.add(redball.body, redball.shape, redball.pivot)
            for yellowball in self.yellowball:
                self.space.add(yellowball.body, yellowball.shape, yellowball.pivot)
        elif self.mode == 1:
            self.space.add(self.cueball.body, self.cueball.shape, self.cueball.pivot)
            for redball in self.redball:
                self.space.add(redball.body, redball.shape, redball.pivot)

        self.input_box = Inputbox()


    def input_handler(self, event):
        self.input_box.input_handler(event)


    def draw(self):
        if self.mode == -1:
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
               self.input_box.angle_input, True, pygame.Color("turquoise"))
            self.display_surface.blit(text, text.get_rect())
            self.draw_line()
        elif self.mode == 1:
            self.display_surface.blit(self.image, (self.x, self.y))
            self.display_surface.blit(
                self.cueball.image, ((self.cueball.body.position.x), (self.cueball.body.position.y)))
            for redball in self.redball:
                self.display_surface.blit(redball.image, ((redball.body.position.x), (redball.body.position.y)))
            text = INPUT_FONT.render(
               self.input_box.angle_input, True, pygame.Color("turquoise"))
            self.display_surface.blit(text, text.get_rect())
            self.draw_line()
        pygame.draw.line(self.display_surface, BLACK, (160, 116), (160, 289), 1)
        pygame.draw.line(self.display_surface, BLACK, (173, 102), (348, 102), 1)
        pygame.draw.line(self.display_surface, BLACK, (370, 102), (546, 102), 1)
        pygame.draw.line(self.display_surface, BLACK, (558, 116), (558, 289), 1)
        pygame.draw.line(self.display_surface, BLACK, (370, 302), (546, 302), 1)
        pygame.draw.line(self.display_surface, BLACK, (173, 302), (348, 302), 1)######
        pygame.draw.line(self.display_surface, BLACK, (160, 116), (152, 110), 1)
        pygame.draw.line(self.display_surface, BLACK, (173, 102), (167, 95), 1)
        pygame.draw.line(self.display_surface, BLACK, (348, 102), (349, 95), 1)
        pygame.draw.line(self.display_surface, BLACK, (370, 102), (369, 95), 1)
        pygame.draw.line(self.display_surface, BLACK, (558, 116), (566, 110), 1)
        pygame.draw.line(self.display_surface, BLACK, (546, 102), (552, 95), 1)
        pygame.draw.line(self.display_surface, BLACK, (558, 289), (566, 294), 1)
        pygame.draw.line(self.display_surface, BLACK, (546, 302), (552, 308), 1)
        pygame.draw.line(self.display_surface, BLACK, (348, 302), (349, 308), 1)
        pygame.draw.line(self.display_surface, BLACK, (370, 302), (369, 308), 1)
        pygame.draw.line(self.display_surface, BLACK, (160, 289), (152, 294), 1)
        pygame.draw.line(self.display_surface, BLACK, (173, 302), (167, 308), 1)


   
    def pocket(self):
        #Red and yellow balls
        if self.mode == -1:
            for pocket in pocket_coords:
                for ball in self.redball:
                    #print(pocket_coords)
                    #print(ball.body.position.x)
                    red_x_dist = abs((ball.body.position.x) - (pocket[0]))
                    red_y_dist = abs((ball.body.position.y) - (pocket[1]))
                    red_dist = math.sqrt((red_x_dist**2) + (red_y_dist**2))
                    if red_dist < POCKET_RADIUS:
                        if self.red_increment == 0:
                            add_coord = self.coords_potted[0]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[1]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[6]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[7]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        self.red_increment += 1
                        self.red_balls_potted += 1
            for pocket in pocket_coords:
                for ball in self.yellowball:
                    yellow_x_dist = abs((ball.body.position.x) - (pocket[0]))
                    yellow_y_dist = abs((ball.body.position.y) - (pocket[1]))
                    yellow_dist = math.sqrt((yellow_x_dist**2) + (yellow_y_dist**2))
                    if yellow_dist < POCKET_RADIUS:
                        if self.yellow_increment == 0:
                            add_coord = self.coords_potted[0]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[1]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[6]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 1:
                            add_coord = self.coords_potted[7]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        self.yellow_increment += 1
                        self.yellow_balls_potted += 1
            for pocket in pocket_coords:
                cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
                cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
                cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
                if cue_dist < POCKET_RADIUS:
                    #print("self.cueball.image")
                    self.cueball.body.position = (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2)
                    self.cueball.body.velocity = (0, 0)
            for pocket in pocket_coords:
                black_x_dist = abs((self.blackball.body.position.x) - (pocket[0]))
                black_y_dist = abs((self.blackball.body.position.y) - (pocket[1]))
                black_dist = math.sqrt((cue_x_dist**2) + (black_y_dist**2))
                if black_dist < POCKET_RADIUS:
                    # if self.red_balls_potted == 7 and self.yellow_balls_potted == 7:
                    #     text = INPUT_FONT.render("Nice Job", True, pygame.color(RED))
                    #     self.display_surface.blit(text, text.get_rect())
                    # else:
                    #     text = INPUT_FONT.render("Your Trash", True, pygame.color(REDE))
                    #     self.display_surface.blit(text, text.get_rect())
                    self.blackball.body.position = (618, 200)
                    self.blackball.body.velocity = (0, 0)


        elif self.mode == 1:
            for pocket in pocket_coords:
                for ball in self.redball:
                    #print("POCKET COORDS --------------------------------------------------------------------------------------------------------------------------------", pocket_coords)
                    #print(ball.body.position.x)
                    red_x_dist = abs((ball.body.position.x) - (pocket[0]))
                    red_y_dist = abs((ball.body.position.y) - (pocket[1]))
                    red_dist = math.sqrt((red_x_dist**2) + (red_y_dist**2))
                    if red_dist < POCKET_RADIUS:
                        if self.red_increment == 0:
                            add_coord = self.coords_potted[0]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[1]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 1:
                            add_coord = self.coords_potted[6]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        self.red_increment += 1
            for pocket in pocket_coords:
                cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
                cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
                cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
                if cue_dist < POCKET_RADIUS:
                    #print("self.cueball.image")
                    self.cueball.body.position = (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2)
                    self.cueball.body.velocity = (0, 0)

    def ball_velocity(self):
        stopped = False
        if self.mode == -1:
            if self.cueball.body.velocity == (0, 0) and self.blackball.body.velocity == (0, 0) and self.redball[0].body.velocity == (0, 0) and self.redball[1].body.velocity == (0, 0) and self.redball[2].body.velocity == (0, 0) and self.redball[3].body.velocity == (0, 0) and self.redball[4].body.velocity == (0, 0) and self.redball[5].body.velocity == (0, 0) and self.redball[6].body.velocity == (0, 0) and self.yellowball[0].body.velocity == (0, 0) and self.yellowball[1].body.velocity == (0, 0) and self.yellowball[2].body.velocity == (0, 0) and self.yellowball[3].body.velocity == (0, 0) and self.yellowball[4].body.velocity == (0, 0) and self.yellowball[5].body.velocity == (0, 0) and self.yellowball[6].body.velocity == (0, 0):
                stopped = True
        elif self.mode == 1:
            if self.cueball.body.velocity == (0, 0) and self.redball[0].body.velocity == (0, 0) and self.redball[1].body.velocity == (0, 0) and self.redball[2].body.velocity == (0, 0) and self.redball[3].body.velocity == (0, 0) and self.redball[4].body.velocity == (0, 0) and self.redball[5].body.velocity == (0, 0):
                stopped = True
        return stopped

    
    def draw_line(self):
        try:
            angle = float(self.input_box.angle_input[7:11])
            #print("Angle:------------------------------------------------------------------------------", angle)
            x_pos = cos(radians(angle))
            y_pos = sin(radians(angle))
            #print("Y_POSITION -------------------------------------------------------------------------------------------------------", y_pos)
            #print("x position", x_pos)
            # print("y position", y_pos)
            # print("INAVLID END POINT", (self.cueball.body.position.x + 25) * x_pos)
            if self.ball_velocity():
                pygame.draw.line(self.display_surface, YELLOW, (self.cueball.body.position.x+5, self.cueball.body.position.y+5), (-(8000 * x_pos)*20, -(8000*y_pos)*20), 1)
        except ValueError:
            pass

    def update(self):
        #print("----------------------------------------------------------------------------------------------------")
        self.pocket()
        # print("Redball:", self.redball[1].body.velocity)
        # print("Cueball:", self.cueball.body.velocity)
        # print("Cueball position y:", self.cueball.body.position.y)
        self.space.step(1/510)
        self.draw_line()
        if self.input_box.play and self.ball_velocity() == True:
            #print("Hello")
            self.cueball.move((self.cueball.body.position), self.input_box.angle_input)
        else:
            pass
        if self.input_box.play:
            self.input_box.play = False

