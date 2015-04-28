import math
class Physics: 
    epsilon = 0.1

    def __init__(self, ent):
        self.ent = ent
        self.fieldDimenX = (self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().x) / 2
        self.fieldDimenZ = self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().z / 2

        self.entities = self.ent.engine.entityMgr.entities
        self.var = 1

    def tick(self, dtime):
        #defined local var for fewer keystrokes
        if (self.ent.mesh == "sphere.mesh"):
            for eid, entity in self.entities.iteritems():
                if (entity.mesh != "sphere.mesh"):
                    dist = self.distance(self.ent.pos.x, entity.pos.x, self.ent.pos.z, entity.pos.z)
                    
                   # print "sphereX: ", self.ent.pos.x, "sphereZ: ", self.ent.pos.z
                    #print "ninja    X : ", entity.pos.x, "ninjaX : ", entity.pos.z
                    #print "dist:    ", dist
                    if dist < 30:
                        print "SUCCESS: ", dist
                        self.var *= -1
                        #issue is here, sphere cant get away in time before next tick, 
                        #updates var causing back and forth
                        if self.var > 0:
                            self.ent.pos.x += 30
                        else:
                            self.ent.pos.x -= 30
            
            self.ent.pos.x += (self.var * 2)

            if self.ent.pos.x > self.fieldDimenX:
                if self.ent.engine.gameMgr.half == 1:
                    self.ent.engine.gameMgr.scoreOne+= 1
                else:
                    self.ent.engine.gameMgr.scoreTwo+= 1
                self.ent.pos.x = 0
                
   
               # print "score", self.score 
            if self.ent.pos.x < -self.fieldDimenX:
                if self.ent.engine.gameMgr.half == 1:
                    self.ent.engine.gameMgr.scoreTwo+= 1
                else:
                    self.ent.engine.gameMgr.scoreOne+= 1
                self.ent.pos.x = 0
                
                
   

        if (self.ent.pos.x > self.fieldDimenX):
            self.ent.pos.x = self.ent.pos.x - 10

        if (self.ent.pos.x < -self.fieldDimenX): 
            self.ent.pos.x = self.ent.pos.x + 10            

        if (self.ent.pos.z > self.fieldDimenZ):
            self.ent.pos.z = self.ent.pos.z - 10

        if (self.ent.pos.z < -self.fieldDimenZ):
            self.ent.pos.z = self.ent.pos.z + 10

    def distance(self, xi,xii,yi,yii):
        sq1 = (xi-xii)*(xi-xii)
        sq2 = (yi-yii)*(yi-yii)
        return math.sqrt(sq1 + sq2)
