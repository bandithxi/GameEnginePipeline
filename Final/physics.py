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
        # print "X: ", self.fieldDimenX, "Z: ", self.fieldDimenZ, "pos: ", self.ent.pos

        if (self.ent.mesh == "sphere.mesh"):
            for eid, entity in self.entities.iteritems():
                if (entity != self):
                    dist = self.distance(self.ent.pos.x, entity.pos.x, self.ent.pos.y, entity.pos.y)
                #print "x2: ", x2, "z2: ", z2
                #print dist
                    if dist < 50:
                        print "dist: ", dist
                        #self.var *= -1
            
            self.ent.pos.x += (self.var * 10)
            print "here"
            if self.ent.pos.x > self.fieldDimenX:
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