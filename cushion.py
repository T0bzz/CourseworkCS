#Imports pymunk
import pymunk

#Creates a cushion object using pykmunk
#Uses a line which allows to create accurate collisions through outlining the cusion (As the cushion is an odd shape which cannot be expressed using a single object)
class Cushion:
    def __init__(self, position):
        self.x, self.y = position
        self.body = pymunk.Body()
        #Creates the line object
        self.shape = pymunk.Segment(self.body, self.x, self.y, 0.1)
        #Sets the density so the ball objects cannot go through the object
        self.shape.density = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        #Impacts the force other objects retain after colliding with the cusion object
        self.shape.elasticity = 0.8
        


        