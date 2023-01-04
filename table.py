import pygame
import pymunk
import math
from math import cos, sin, tan, radians
from config import *
from cushion import Cushion
from ball import Cueball, Red_Ball, Yellow_Ball, Black_Ball
from inputbox import Inputbox


class Table:
    def __init__(self, game, engine, screen, display_surface, x, y, mode, settings, red_balls_potted, yellow_balls_potted, level_balls):
        self.x = x
        self.y = y
        self.game = game
        self.screen = screen
        self.red_increment = 0
        self.yellow_increment = 0
        self.red_balls_potted = red_balls_potted
        self.yellow_balls_potted = yellow_balls_potted
        self.mode = mode
        self.settings = settings
        self.level_balls = level_balls
        self.display_surface = display_surface
        self.coords_potted = [0, 30, 60, 90, 120, 150, 180]
        self.direction = DIRECTION
        self.cushions = [Cushion(CUSHION1), Cushion(CUSHION2), Cushion(
            CUSHION3), Cushion(CUSHION4), Cushion(CUSHION5), Cushion(CUSHION6), Cushion(S_CP_TL_1), Cushion(S_CP_TL_2), Cushion(S_MP_T_1), Cushion(S_MP_T_2), Cushion(S_CP_TR_1), Cushion(S_CP_TR_2), Cushion(S_CP_BR_1), Cushion(S_CP_BR_2), Cushion(S_MP_B_1), Cushion(S_MP_B_2), Cushion(S_CP_BL_1), Cushion(S_CP_BL_2)]
        self.space = pymunk.Space()
        self.static_body = self.space.static_body
        self.engine = engine
        self.image = pygame.image.load(
            path.join(TABLE_FOLDER, "Table.png")).convert_alpha()
        self.cueball = Cueball(260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2, 5, self.static_body)
        if self.mode == -1:
            self.redball = [Red_Ball(RED1, 5, self.static_body), Red_Ball(RED2, 5, self.static_body), Red_Ball(RED3, 5, self.static_body), Red_Ball(RED4, 5, self.static_body), Red_Ball(RED5, 5, self.static_body), Red_Ball(RED6, 5, self.static_body), Red_Ball(RED7, 5, self.static_body)]
            self.yellowball = [Yellow_Ball(Yellow1, 5, self.static_body), Yellow_Ball(Yellow2, 5, self.static_body), Yellow_Ball(Yellow3, 5, self.static_body), Yellow_Ball(Yellow4, 5, self.static_body), Yellow_Ball(Yellow5, 5, self.static_body), Yellow_Ball(Yellow6, 5, self.static_body), Yellow_Ball(Yellow7, 5, self.static_body)]
            self.blackball = Black_Ball(Black1, 5, self.static_body)
        elif self.mode == 1:
            self.redball = [Red_Ball(level_balls[0], 5, self.static_body), Red_Ball(level_balls[1], 5, self.static_body), Red_Ball(level_balls[2], 5, self.static_body), Red_Ball(level_balls[3], 5, self.static_body), Red_Ball(level_balls[4], 5, self.static_body), Red_Ball(level_balls[5], 5, self.static_body)]    
        self.GameOver = self.Game_Over()

        #Adds objects to the pymunk space, allowing collisions to take place
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

        self.input_box = Inputbox(game)

    #Calls the input_handler_angle function from input_box
    def input_handler(self, event):
        self.input_box.input_handler_angle(event)

    #Draws objects on the screen, including balls, the pool table and the input box
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
        text_angle_type = INPUT_FONT.render(self.angle_type(), True, pygame.Color("turquoise"))
        self.display_surface.blit(text_angle_type, (0, 35))
        text_instructions_1 = INPUT_FONT.render("Press 'SPACE' to return to the main menu", True, pygame.Color("turquoise"))
        self.display_surface.blit(text_instructions_1, (150, 0))
        text_instructions_2 = INPUT_FONT.render("Press 'ENTER' to fire the cueball", True, pygame.Color("turquoise"))
        self.display_surface.blit(text_instructions_2, (150, 35))

   #Potts balls when the are in a given range, aswell as re-drawing the balls in certain positions based on the mode
    def pocket(self):
        #Red and yellow balls
        if self.mode == -1:
            for pocket in pocket_coords:
                for ball in self.redball:
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
                        elif self.red_increment == 2:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 3:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 4:
                            add_coord = self.coords_potted[4]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 5:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 6:
                            add_coord = self.coords_potted[6]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
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
                        elif self.yellow_increment == 2:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 3:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 4:
                            add_coord = self.coords_potted[4]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 5:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        elif self.yellow_increment == 6:
                            add_coord = self.coords_potted[6]
                            ball.body.position = (YELLOWS[0] + add_coord, YELLOWS[1])
                            ball.body.velocity = (0, 0)
                        self.yellow_increment += 1
                        self.yellow_balls_potted += 1
            for pocket in pocket_coords:
                cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
                cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
                cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
                if cue_dist < POCKET_RADIUS:
                    self.cueball.body.position = (5,70)
                    self.cueball.body.velocity = (0, 0)
                    if self.ball_velocity() == True:
                        self.cueball.body.position = (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2)
                        self.cueball.body.velocity = (0, 0)
            for pocket in pocket_coords:
                black_x_dist = abs((self.blackball.body.position.x) - (pocket[0]))
                black_y_dist = abs((self.blackball.body.position.y) - (pocket[1]))
                black_dist = math.sqrt((black_x_dist**2) + (black_y_dist**2))
                if black_dist < POCKET_RADIUS:
                    self.blackball.body.position = (618, 200)
                    self.blackball.body.velocity = (0, 0)
        elif self.mode == 1:
            for pocket in pocket_coords:
                for ball in self.redball:
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
                        elif self.red_increment == 2:
                            add_coord = self.coords_potted[2]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 3:
                            add_coord = self.coords_potted[3]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 4:
                            add_coord = self.coords_potted[4]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        elif self.red_increment == 5:
                            add_coord = self.coords_potted[5]
                            ball.body.position = (REDS[0] + add_coord, REDS[1])
                            ball.body.velocity = (0, 0)
                        self.red_increment += 1
                        self.red_balls_potted += 1
        for pocket in pocket_coords:
            cue_x_dist = abs((self.cueball.body.position.x) - (pocket[0]))
            cue_y_dist = abs((self.cueball.body.position.y) - (pocket[1]))
            cue_dist = math.sqrt((cue_x_dist**2) + (cue_y_dist**2))
            if cue_dist < POCKET_RADIUS:
                self.cueball.body.position = (0, 70)
                self.cueball.body.velocity = (0, 0)
                if self.ball_velocity() == True:
                    self.cueball.body.position = (260 - BALL_RADIUS * 2, 209 - BALL_RADIUS * 2)
                    
    #This function is used to detirmine whther or not the balls are stationary
    def ball_velocity(self):
        stopped = False
        if self.mode == -1:
            if self.cueball.body.velocity == (0, 0) and self.blackball.body.velocity == (0, 0) and self.redball[0].body.velocity == (0, 0) and self.redball[1].body.velocity == (0, 0) and self.redball[2].body.velocity == (0, 0) and self.redball[3].body.velocity == (0, 0) and self.redball[4].body.velocity == (0, 0) and self.redball[5].body.velocity == (0, 0) and self.redball[6].body.velocity == (0, 0) and self.yellowball[0].body.velocity == (0, 0) and self.yellowball[1].body.velocity == (0, 0) and self.yellowball[2].body.velocity == (0, 0) and self.yellowball[3].body.velocity == (0, 0) and self.yellowball[4].body.velocity == (0, 0) and self.yellowball[5].body.velocity == (0, 0) and self.yellowball[6].body.velocity == (0, 0):
                stopped = True
        elif self.mode == 1:
            if self.cueball.body.velocity == (0, 0) and self.redball[0].body.velocity == (0, 0) and self.redball[1].body.velocity == (0, 0) and self.redball[2].body.velocity == (0, 0) and self.redball[3].body.velocity == (0, 0) and self.redball[4].body.velocity == (0, 0) and self.redball[5].body.velocity == (0, 0):
                stopped = True
        return stopped
        
    #Function is used to detirmine whther or not the black ball has been pottedand when to restart the program
    def Game_Over(self):
        GameOver = False
        if self.mode == -1:
            if self.red_balls_potted != 7 and self.yellow_balls_potted != 7 and self.blackball.body.position == (618, 200):
                GameOver = True
            elif self.red_balls_potted == 7 and self.yellow_balls_potted == 7 and self.blackball.body.position == (618, 200):
                GameOver = True
            else:
                pass
        elif self.mode == 1:
            if self.red_balls_potted == 6:
                GameOver = True
        return GameOver

    #Draws the line used for aiming based whther the difficulty is set to hard or not
    def draw_line(self):
        if self.settings.hard_mode == False:
            try:
                angle = float(self.input_box.angle_input[7:11])
                x_pos = cos(radians(angle))
                y_pos = sin(radians(angle))
                if self.ball_velocity():
                    pygame.draw.line(self.display_surface, YELLOW, (self.cueball.body.position.x+5, self.cueball.body.position.y+5), (-(self.cueball.force * x_pos)*20, -(self.cueball.force*y_pos)*20), 1)
            except ValueError:
                pass

    def angle_type(self):
        angle_type = ""
        try:
            if (float(self.input_box.angle_input[7:10])) % 360 == 90 or (float(self.input_box.angle_input[7:10])) % 360 == 270:
                angle_type = "Right Angle"
            elif (float(self.input_box.angle_input[7:10])) % 360 <= 90:
                angle_type = "Acute"
            elif (float(self.input_box.angle_input[7:10])) % 360 > 90 and (float(self.input_box.angle_input[7:10])) % 360 <= 180:
                angle_type = "Obtuse"
            elif (float(self.input_box.angle_input[7:10])) % 360 > 180:
                angle_type = "Reflex"
        except ValueError:
            pass
        return angle_type
        

    #This subroutine is used to continuously update the game, calling necessary functions constantly, allowing the program to run animations smoothly and run checks such as check potted constantly
    def update(self):
        self.pocket()
        self.space.step(1/520)
        self.draw_line()
        self.angle_type()
        if self.input_box.play and self.ball_velocity() == True:
            #print("Hello")
            self.cueball.move((self.cueball.body.position), self.input_box.angle_input)
        else:
            pass
        if self.input_box.play:
            self.input_box.play = False
        if self.Game_Over() == True:
            self.game.start()
        

