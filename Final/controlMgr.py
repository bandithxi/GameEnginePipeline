import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import random as rand
import pygame

class ControlMgr:

    def __init__(self, engine):
    	#print "__init__ ControlMgr"
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.Keyboard = engine.inputMgr.keyboard
        self.sceneManager = engine.gfxMgr.sceneManager
        self.pressed = False 
        self.heldTime = 0
        
        #changed
        self.JS_A_Pressed = False
            
    def init(self): 
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        self.debug = 0
        for i in range(joystick_count):
            self.joystick = pygame.joystick.Joystick(i)
            self.joystick.init()
            self.buttons = self.joystick.get_numbuttons()
            self.axes = self.joystick.get_numaxes()
        #print "joystick count: ", joystick_count

    def handleEntitiesController(self, dt):
    	# print "called handleEntitiesController"
        selectedEnt = self.entityMgr.selectedEntities

    	if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) or self.Keyboard.isKeyDown(OIS.KC_I):
            for ent in selectedEnt:
                ent.desiredSpeed += 100 * dt
                #print "keyboard", ent.desiredSpeed, dt
        
        if not self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) and not self.Keyboard.isKeyDown(OIS.KC_I):
            for ent in selectedEnt:
                pass
                #ent.desiredSpeed = 0


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

        #reset ball position for debugging
        if self.Keyboard.isKeyDown(OIS.KC_H):
            for eid, ent in self.entityMgr.entities.iteritems():
                if (ent.uiname == "Ball"):
                    ent.pos = ogre.Vector3(0,0,0)

        # changed
        someJoyButton = False
        for event in pygame.event.get(): # User did something
            pass

        for i in range( self.buttons ):
            button = self.joystick.get_button(i)
            if button == 1:
                someJoyButton = True
                self.pressed = True
        self.JS_A_Pressed = someJoyButton

        for i in range (self.axes):
            axis = self.joystick.get_axis(i)
            if i == 0:
                if axis < -.5:
                    #print "left"
                    for ent in selectedEnt: 
                        ent.desiredHeading += 100 * dt
                        # Ensure we work with angles 0 to 360
                        if ent.desiredHeading > 360:
                            # Heading is also decrease by 360 for simpler physics logic 
                           
                            ent.desiredHeading -= 360  
                            ent.heading -= 360     

                elif axis > .5:
                    #print "right" 
                    for ent in selectedEnt: 
                        ent.desiredHeading -= 100 * dt
                        if ent.desiredHeading < 0:
                            ent.desiredHeading += 360  
                            ent.heading += 360 

            elif i == 1:
                if axis < -.5:
                    #print "up"
                    for ent in selectedEnt:
                        ent.desiredSpeed += 200 * dt
                        #print ent.desiredSpeed, dt 

                else:# axis > .5:
                    #print "down"
                    for ent in selectedEnt:
                        ent.desiredSpeed = 0 

        if self.pressed:
            self.heldTime += 2.0 * dt
            if self.heldTime > 2.0:  
                self.heldTime = 2.0

        if (not self.Keyboard.isKeyDown(OIS.KC_SPACE) and not self.JS_A_Pressed) and self.pressed:  
            for eid, ent in self.entityMgr.entities.iteritems():
                    if (ent.uiname == "Ball"):
                        #print "Here1"
                        if (ent.attachEnt != None):   
                            ent.heading = ent.attachEnt.heading
                            ent.desiredHeading = ent.heading + rand.uniform(-20*self.heldTime, 20*self.heldTime)
                            #print "Here2"
                            ent.attachEnt = None
                            ent.toggle = 3.0
                    
                            self.pressed = False
                        
                            if self.heldTime > 1.1:
                                ent.speed = ent.maxSpeed * self.heldTime
                                #print "Here3" 
                                ent.vel.y = 1000.0 * self.heldTime / 2.0
                            else:
                                #print "Here4"
                                ent.speed = ent.maxSpeed * 2.0 * self.heldTime
                            
                            #print ent.speed
                            ent.desiredSpeed = 0
                            self.heldTime = 0
                        else:
                            #print "Here5"
                            pass

                        

            
                
            
          
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
