import math
class Physics: 
    epsilon = 0.1

    def __init__(self, ent):
        self.ent = ent
        self.fieldDimenX = (self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().x) / 2
        self.fieldDimenZ = self.ent.engine.gfxMgr.groundEnt.getBoundingBox().getSize().z / 2

        self.entities = self.ent.engine.entityMgr.entities
        self.var = 1
        self.grassOffSet = 300

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
        
        self.boundaryCheck()
        self.collisionCheck()
   
        if (self.ent.mesh == "sphere.mesh"):
            if (self.ent.attachEnt != None): #if player has ball then move ball
                self.ent.pos = self.ent.attachEnt.pos
          #      pass
            else: # if he doesn't decr time until he is allowed
                if (self.ent.toggle <= 0.0): 
                    self.ent.toggle = 0.0
                    
                 #   print "here"

                else:
                    self.ent.toggle -= dtime
                #    print "there"
            
        #print "ent.pos", self.ent.pos
        #print "ent.velo", self.ent.vel

    def distance(self, xi,xii,yi,yii):
        sq1 = (xi-xii)*(xi-xii)
        sq2 = (yi-yii)*(yi-yii)
        return math.sqrt(sq1 + sq2)

   
    def collisionCheck(self):
        for eid, ball in self.entities.iteritems():
            if (ball.mesh == "sphere.mesh" and self.ent.hasAnimation):
                dist = self.distance(self.ent.pos.x, ball.pos.x, self.ent.pos.z, ball.pos.z)
                    
                   # print "sphereX: ", self.ent.pos.x, "sphereZ: ", self.ent.pos.z
                    #print "ninja    X : ", entity.pos.x, "ninjaX : ", entity.pos.z
                    #print "dist:    ", dist
                if dist < 75:
                        #print "SUCCESS: ", dist
                    self.var *= -1
                        #issue is here, sphere cant get away in time before next tick, 
                        #updates var causing back and forth
                    if (ball.toggle <= 0.0): #if ball is allowed to be held then attach to a player
                     #   print "collision"
                        
                        ball.attachEnt = self.ent 
                   # if self.var > 0:
                    #    self.ent.pos.y += 30
                     
                    #else:
                     #   self.ent.pos.y -= 30
            
            #self.ent.pos.x += (self.var * 2)
         
        
        pass

    def boundaryCheck(self):
        if (self.ent.mesh == "sphere.mesh"):
            #print "sphere check"
            
            #print self.ent.pos.x
            if self.ent.pos.x > self.fieldDimenX - self.grassOffSet:
                #check goal
                #print "right check"
                #print self.ent.pos.x
                if self.ent.engine.gameMgr.half == 1:
                    self.ent.engine.gameMgr.scoreOne+= 1
                else:
                    self.ent.engine.gameMgr.scoreTwo+= 1
                
                self.ent.pos.x = self.ent.pos.y = self.ent.pos.z = 0
                self.ent.speed = 0


                #o.w. out of bounds 
                    #set ball for goal kick
                    #dist of all players are > goal box
                
   
               # print "score", self.score 
            if self.ent.pos.x < -self.fieldDimenX + self.grassOffSet:
                #check goal
                if self.ent.engine.gameMgr.half == 1:
                    self.ent.engine.gameMgr.scoreTwo+= 1
                else:
                    self.ent.engine.gameMgr.scoreOne+= 1
                self.ent.pos.x = self.ent.pos.y = self.ent.pos.z = 0

                self.ent.speed = 0
                
        #if (self.ent.mesh == "ninja.mesh"):
         #   for eid, entity in self.entities.iteritems():
          #      if (entity.mesh == "sphere.mesh"):
           #         self.ent.pos.z = entity.pos.z


       # if (self.ent.pos.x > self.fieldDimenX):
        #    self.ent.pos.x = self.ent.pos.x - 10

        #if (self.ent.pos.x < -self.fieldDimenX): 
         #   self.ent.pos.x = self.ent.pos.x + 10            

        if (self.ent.pos.z > self.fieldDimenZ - self.grassOffSet):
            self.ent.pos.z = self.fieldDimenZ - self.grassOffSet
            self.ent.vel.x = 0
            self.ent.vel.z = 0

        if (self.ent.pos.z < -self.fieldDimenZ + self.grassOffSet):
            self.ent.pos.z = -self.fieldDimenZ + self.grassOffSet
            self.ent.vel.x = 0
            self.ent.vel.z = 0
        pass

    def goalCheck(self):
        #check y, z bounds
        pass        

