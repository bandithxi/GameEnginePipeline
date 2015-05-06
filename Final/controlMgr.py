import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import random as rand
import utils
import AIaction as action

class ControlMgr:

    def __init__(self, engine):
    	#print "__init__ ControlMgr"
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.Keyboard = engine.inputMgr.keyboard
        self.sceneManager = engine.gfxMgr.sceneManager
        self.pressed = False 
        self.heldTime = 0
        
            
    def init(self): 
        
    	pass

    def handleEntitiesController(self, dt):
    	# print "called handleEntitiesController"
        team1 = self.entityMgr.team1

    	if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) or self.Keyboard.isKeyDown(OIS.KC_I):
            for key, ent in team1.iteritems():
                if (ent == self.entityMgr.selectedEntP1):    
                    ent.desiredSpeed += 100 * dt
                else:
                    ent.desiredSpeed = 0
        
        if not self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) and not self.Keyboard.isKeyDown(OIS.KC_I):
            ent = self.entityMgr.selectedEntP1
            
            if (ent != None):
                ent.desiredSpeed = 0.0


        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD4) or self.Keyboard.isKeyDown(OIS.KC_J):
            
            ent = self.entityMgr.selectedEntP1
            ent.desiredHeading += 100 * dt
                
            # Ensure we work with angles 0 to 360
            if ent.desiredHeading > 360:
            # Heading is also decrease by 360 for simpler physics logic 
                   
                ent.desiredHeading -= 360  
                ent.heading -= 360      
                     

        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD6) or self.Keyboard.isKeyDown(OIS.KC_L):
            
            ent = self.entityMgr.selectedEntP1
            ent.desiredHeading -= 100 * dt
                
            # Ensure we work with angles 0 to 360
            if ent.desiredHeading < 0:
                ent.desiredHeading += 360  
                ent.heading += 360 
                #  if ent.heading < 0:
                #     ent.heading += 360
            
        
        
        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.pressed = True
            #print dt
            self.heldTime += 2.0 * dt
            if self.heldTime > 2.0:  
                self.heldTime = 2.0
            pass
         
        if not self.Keyboard.isKeyDown(OIS.KC_SPACE) and self.pressed:
               
  
                #for eid, ent in self.entityMgr.entities.iteritems():
                 #       if (ent.uiname == "Ball"):
                            #print "Here1"
                            ent = self.entityMgr.ball
                            if (ent.attachEnt != None):
                                
                                teammate = ent.attachEnt.nearestTeamate()
                                distance = 1000000 # 
                                
                                if (teammate):
                                    distance = utils.distance(ent.attachEnt, teammate)
                                    #distance = 1000000
                                
                                #1/4 s short pass
                                if (self.heldTime < .5 and distance < 600.0):
                                    print "short pass"
                                    self.engine.entityMgr.addAction(ent, action.Intercept(ent, teammate))

                                    pass

                                else:    
                                    ent.heading = ent.attachEnt.heading
                                    ent.desiredHeading = ent.heading + rand.uniform(-20*self.heldTime, 20*self.heldTime)
                                #print "Here2"
                                    #1/2 s or longer and the ball will rise
                                    if self.heldTime > 1.1:
                                        ent.speed = ent.maxSpeed * self.heldTime
                                    #print "Here3" 
                                        ent.vel.y = 1000.0 * self.heldTime / 2.0
                                    else:
                                    #print "Here4"
                                        ent.speed = ent.maxSpeed * 2.0 * self.heldTime

                                    # team mate will try to interscept
                                    #if (teammate):
                                     #   self.engine.entityMgr.addAction(teammate, action.Intercept(teammate, ent))
                                
                                #print ent.speed
                                ent.desiredSpeed = 0
                                self.heldTime = 0
                                ent.attachEnt = None
                                ent.toggle = .2
                        
                                self.pressed = False
                                
                                
                            else:
                                #print "Here5"
                                pass

                        

            
                
            
          
        #for ent in selectedEnt:
            #Metrics
         #   pass
           # print 'heading:', ent.heading
           # print 'desired heading:', ent.desiredHeading
            #print 'max speed: ', ent.maxSpeed
            #print 'desired speed: ', ent.desiredSpeed
            #print 'speed: ', ent.speed
            #print str(ent.pos)
        
    def tick(self, dt):
        self.handleEntitiesController(dt)

    def stop(self):
        pass


