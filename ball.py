import pygame
from config import *
import pymunk
from math import sin, cos, tan


class Cueball:
    def __init__(self, x, y, mass, static_body):
        self.x = x 
        self.y = y 
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))
        self.shape.elasticity = 0.9
        self.shape.mass = mass
        self.body.position = (self.x, self.y)
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 1200
        
                
    # def move(self, temp_pos, eq):
    #     self.body.apply_impulse_at_local_point((100, 0))
    #     temp_pos = (self.body.position.x, self.body.position.y)
    #     x = self.body.position.x
    #     try:
    #         y = eval(eq[3:]) # Skips 'y ='
    #         self.body.position = x, y
    #         print("Test1")
    #         print("Test2")
    #         if type(self.y) not in (int, float):
    #             raise Exception("Unexpected eval() return")
    #     except:
    #         x, y = temp_pos  # Dont move if equation is invalid
            

class Red_Ball(Cueball):
    def __init__(self, position, mass, static_body):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        self.image = pygame.image.load(path.join(BALL_FOLDER, "Redball.png"))
        self.shape.elasticity = 0.9
        self.shape.mass = mass
        self.body.position = (position)
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 1000
            
    def move():
        pass



class Yellow_Ball(Cueball):
    def __init__(self, position, mass, static_body):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        self.image = pygame.image.load(path.join(BALL_FOLDER, "Yellowball.png"))
        self.shape.elasticity = 0.9
        self.shape.mass = mass
        self.body.position = (position)
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 1000
            
    def move():
        pass

class Black_Ball(Cueball):
    def __init__(self, position, mass, static_body):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        self.image = pygame.image.load(path.join(BALL_FOLDER, "Blackball.png"))
        self.shape.elasticity = 0.9
        self.shape.mass = mass
        self.body.position = (position)
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 1000
            
    def move():
        pass