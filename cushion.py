import pymunk

class Cushion:
    def __init__(self, position):
        self.x, self.y = position
        self.body = pymunk.Body()
        self.shape = pymunk.Segment(self.body, self.x, self.y, 0.1)
        self.shape.friction = 10
        self.shape.density = 10000000000000000000000000000000
        self.shape.elasticity = 0.8
        


        