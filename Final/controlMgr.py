import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS


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
        selectedEnt = self.entityMgr.selectedEntities

    	if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) or self.Keyboard.isKeyDown(OIS.KC_I):
            for ent in selectedEnt:
                ent.desiredSpeed += 100 * dt
        
        if not self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) and not self.Keyboard.isKeyDown(OIS.KC_I):
            for ent in selectedEnt:
                ent.desiredSpeed = 0


        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD4) or self.Keyboard.isKeyDown(OIS.KC_J):
            for ent in selectedEnt: 
                ent.desiredHeading += 100 * dt
                # Ensure we work with angles 0 to 360
                if ent.desiredHeading > 360:
                    # Heading is also decrease by 360 for simpler physics logic 
                   
                    ent.desiredHeading -= 360  
                    ent.heading -= 360      
                     

        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD6) or self.Keyboard.isKeyDown(OIS.KC_L):
            for ent in selectedEnt: 
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
            for eid, ent in self.entityMgr.entities.iteritems():
                    if (ent.uiname == "Ball"):  
                         
                            self.pressed = False
                  
                            if self.heldTime > 1.1:
                                ent.speed = ent.maxSpeed * self.heldTime
                                
                                ent.vel.y = 1000.0 * self.heldTime / 2.0
                            else:
                                
                                ent.speed = ent.maxSpeed * 2.0 * self.heldTime
                                
                                #print ent.speed
                            ent.desiredSpeed = 0
                            self.heldTime = 0
                        

            
                
            
          
        for ent in selectedEnt:
            #Metrics
            pass
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
