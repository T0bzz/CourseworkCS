#Imports necessary libraries and classes
import pygame
from config import *
import pymunk
#importing sin, cos and radians means math.___ is n ot needed during the code
from math import sin, cos, radians

#Creates the class Cueball which defines the image and properties of the object using the pymunk library
class Cueball:
    def __init__(self, x, y, mass, static_body):
        self.x = x 
        self.y = y 
        #Defines the pymunk body as a circles with the same radius as the image used
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, BALL_RADIUS)
        #Loads the image for the cueball object
        self.image = pygame.image.load(path.join(CUEBALL_FOLDER, "Cueball.png"))
        #Sets properties for the object
        self.shape.elasticity = 0.9 #Amount of force kept after a collision
        self.shape.mass = mass #Mass of the abject which affects the impact of the apply_impulse_at_local_point
        self.body.position = (self.x, self.y)#Sets the position of the object as self.x and self.y, this means that the body and the image are positioned together
        #Cretes a pivot joint used to replicate friction acting on the pymunk objects
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 1200
        self.force = FORCE
        
    #Function used to apply a force on the cudeball object based upon the angle inputed by the user
    def move(self, pos, angle):
        try:
            self.angle = float(angle[7:11])
            #Uses trigonometry and radians to create an x and y position based on the angle inputted
            self.x_impulse = cos(radians(self.angle))
            self.y_impulse = sin(radians(self.angle))
            #Applies an impulse on an object. Negatives are used to reverse the direction of force
            self.body.apply_impulse_at_local_point((-(self.force*self.x_impulse), -(self.force*self.y_impulse)))
        except ValueError:
            pass
        
            
#Creetes a redball class using polymorphism and inheritence
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


#Creates a yellow ball class using polymorhism and inheritance
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

#Creates a blackball object using polymorphism and inheritance
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