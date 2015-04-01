from vector import MyVector

class Physics:
    def __init__(self, creator):
        self.creator = creator

    def update(self, dTime):
        #set local variables 
        oldPos = self.creator.pos
        velocity = self.creator.vel
        
        #perform physic operation
        newPos = oldPos + velocity * dTime
        
        #update entity
        self.creator.pos = newPos

