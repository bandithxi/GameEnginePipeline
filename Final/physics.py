import math
class Physics: 
    epsilon = 0.1

    def __init__(self, ent):
        self.ent = ent
        
    def tick(self, dtime):
        #print "Physics tick", dtime
        
        #defined local var for fewer keystrokes
        
        if (self.ent.mesh == "sphere.mesh"):
            self.ent.pos.x += 10 
        
        if (self.ent.pos.x > 1800):
            self.ent.pos.x = 0
