import math
class Physics: 
    epsilon = 0.1

    def __init__(self, ent):
        self.ent = ent
        self.fieldDimenX = (self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().x) / 2
        self.fieldDimenZ = self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().z / 2

        
    def tick(self, dtime):
        #defined local var for fewer keystrokes
        # print "X: ", self.fieldDimenX, "Z: ", self.fieldDimenZ, "pos: ", self.ent.pos

        if (self.ent.mesh == "sphere.mesh"):
            self.ent.pos.x += 5

        if (self.ent.pos.x > self.fieldDimenX):
            self.ent.pos.x = self.ent.pos.x - 10

        if (self.ent.pos.x < -self.fieldDimenX): 
            self.ent.pos.x = self.ent.pos.x + 10            

        if (self.ent.pos.z > self.fieldDimenZ):
            self.ent.pos.z = self.ent.pos.z - 10

        if (self.ent.pos.z < -self.fieldDimenZ):
            self.ent.pos.z = self.ent.pos.z + 10