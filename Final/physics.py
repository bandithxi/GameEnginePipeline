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
        #print "Physics tick", dtime
        
        #defined local var for fewer keystrokes
        
        speed = self.ent.speed
        gravity = 8 #4
        acc = self.ent.acceleration 
        maxSpeed = self.ent.maxSpeed
        desiredHeading = self.ent.desiredHeading

        heading = self.ent.heading
        tRate = self.ent.turningRate 
        
        if maxSpeed < self.ent.desiredSpeed:
            self.ent.desiredSpeed = maxSpeed
        elif 0 > self.ent.desiredSpeed:
            self.ent.desiredSpeed = 0      
        
        desiredSpeed = self.ent.desiredSpeed
        #print 'desired speed: ', desiredSpeed
        if abs(desiredSpeed - speed) > self.epsilon: 
            if desiredSpeed > speed:
                speed += (acc * dtime)
            elif desiredSpeed < speed:
                speed -= (acc * dtime)
        elif desiredSpeed == 0:
            speed = 0

        self.ent.speed = speed
        #print 'speed: ', self.ent.speed

        if abs(desiredHeading - heading) > self.epsilon:
            dHead = (tRate * dtime)
            
            if desiredHeading > heading:
                heading += dHead
            elif desiredHeading < heading:
                heading -= dHead
                dHead = dHead * -1
        else:
            dHead = 0
        
        self.ent.heading = heading
        self.ent.deltaHeading = dHead
        
        
        if (self.ent.pos.y > 25.0):
            self.ent.vel.y -= gravity
        elif (self.ent.pos.y < 25.0):
            if (self.ent.vel.x > 0):
                self.ent.vel.y = -self.ent.vel.y / 2.0
            else:
                self.ent.vel.y = 0.0
            self.ent.pos.y = 25.0
            pass

            
        #print self.ent.vel.y
        self.ent.vel.x = speed * math.cos(heading/180*3.14)
        self.ent.vel.z = -speed * math.sin(heading/180*3.14)

        self.ent.pos = self.ent.pos + (self.ent.vel * dtime)
        
        if (self.ent.pos.x > self.fieldDimenX):
            self.ent.pos.x = -3200
        
        #print "ent.pos", self.ent.pos
        #print "ent.velo", self.ent.vel

    def distance(self, xi,xii,yi,yii):
        sq1 = (xi-xii)*(xi-xii)
        sq2 = (yi-yii)*(yi-yii)
        return math.sqrt(sq1 + sq2)
