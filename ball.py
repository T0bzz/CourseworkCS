import pygame
from config import *
import pymunk
from math import sin, cos, tan, degrees, radians


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
        self.pivot.max_force = 1200#
        self.force = 8000
        
        
                
    def move(self, pos, angle):
        try:
            self.angle = float(angle[7:11])
            #print("This is the angle input:", self.angle)
            self.x_impulse = cos(radians(self.angle))
            self.y_impulse = sin(radians(self.angle))
            #print("Y impulse ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------", self.y_impulse)
            self.body.apply_impulse_at_local_point((-(self.force*self.x_impulse), -(self.force*self.y_impulse)))
        except ValueError:
            pass
        
            

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
        self.pivot.max_force = 1200
            
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
        self.pivot.max_force = 1200
            
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
        self.pivot.max_force = 1200
            
    def move():
        pass