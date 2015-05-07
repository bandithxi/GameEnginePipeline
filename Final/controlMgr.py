import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import random as rand
import pygame
import utils
import AIaction as action

#JS_AXIS_Y = 1
#JS_AXIS_X = 0
#JS_AXIS_UP = -.2
#JS_AXIS_DOWN = .2
#JS_AXIS_LEFT = -.2
#JS_AXIS_RIGHT = .2
#JS_BUTTON_A = 1
#JS_BUTTON_B = 2

class ControlMgr:

    def __init__(self, engine):
        #print "__init__ ControlMgr"
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.Keyboard = engine.inputMgr.keyboard
        self.sceneManager = engine.gfxMgr.sceneManager
        self.pressed = False 
        self.heldTime = 0
        self.slide = False
            
    def init(self):
        pygame.joystick.init()
        self.num_joysticks = pygame.joystick.get_count()
        self.debug = 0
        self.js = []
        self.p1UseJoystick = False
        self.p2UseJoystick = False
        self.JS_Pressed_A = True

        for i in range(self.num_joysticks):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.js.append(joystick)

        #print "num joysticks ", self.num_joysticks

    def handleEntitiesController(self, dt):
        # print "called handleEntitiesController"
        team1 = self.entityMgr.team1
        ent = None

        someJoyButton = False
        for i in range(self.num_joysticks):
            # print i
            if (i == 0 and self.entityMgr.selectedEntP1):
                #print "one player"
                ent = self.entityMgr.selectedEntP1
                self.p1UseJoystick = True
            if (i == 1 and self.entityMgr.selectedEntP2):
                #print "two player"
                ent = self.entityMgr.selectedEntP2
                self.p2UseJoystick = True

            buttons = self.js[i].get_numbuttons()
            axis = self.js[i].get_numaxes()

            for event in pygame.event.get():
                pass

            if (self.js[i].get_axis(0) and self.js[i].get_axis(0) < 0 ):
                #print "left"
                ent.desiredHeading += 100 * dt
                if ent.desiredHeading > 360:
                    ent.desiredHeading -= 360  
                    ent.heading -= 360     

            elif (self.js[i].get_axis(0) and self.js[i].get_axis(0) > 0 ):
                #print "right"
                ent.desiredHeading -= 100 * dt
                if ent.desiredHeading < 360:
                    ent.desiredHeading += 360  
                    ent.heading += 360     

            elif (self.js[i].get_axis(1) and self.js[i].get_axis(1) < 0 ):
                #print "up"
                ent.desiredSpeed += 100 * dt
                ent.speed += ent.maxSpeed * dt

            else:
                #print "down"
                if(ent != None):
                    ent.desiredSpeed = 0


            if (self.js[i].get_button(1)):
                #print "A"
                someJoyButton = True
                self.pressed = True
                self.heldTime += 2.0 * dt
                if self.heldTime > 2.0:  
                    self.heldTime = 2.0
            self.JS_Pressed_A = someJoyButton

        if not self.p1UseJoystick:
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
                    # Heading is also decrease by 360 for simpler physics logic 
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
         
        if (not self.Keyboard.isKeyDown(OIS.KC_SPACE) and not self.JS_Pressed_A ) and self.pressed:    
  
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
                                if (self.heldTime < .5 and distance < 1200.0):
                                    #print "short pass"
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
            #pass
            #print 'heading:', ent.heading
            #print 'desired heading:', ent.desiredHeading
            #print 'max speed: ', ent.maxSpeed
            #print 'desired speed: ', ent.desiredSpeed
            #print 'speed: ', ent.speed
            #print str(ent.pos)
        
    def tick(self, dt):
        self.handleEntitiesController(dt)

    def stop(self):
        pass
