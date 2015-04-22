import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class ControlMgr:

    def __init__(self, engine):
    	print "__init__ ControlMgr"
        self.engine = engine
        self.entityMgr = engine.entityMgr
        self.Keyboard = engine.inputMgr.keyboard
        self.sceneManager = engine.gfxMgr.sceneManager

    def init(self): 
    	pass

    def handleEntitiesController(self, dt):
    	# print "called handleEntitiesController"

        selectedEnt = self.entityMgr.selectedEntities
    	if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8) or self.Keyboard.isKeyDown(OIS.KC_I):
            for ent in selectedEnt:
                ent.pos.z -= 100 * dt

        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD2) or self.Keyboard.isKeyDown(OIS.KC_K):
            for ent in selectedEnt: 
                ent.pos.z += 100 * dt
        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD4) or self.Keyboard.isKeyDown(OIS.KC_J):
            for ent in selectedEnt: 
                ent.pos.x -= 100 * dt

        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD6) or self.Keyboard.isKeyDown(OIS.KC_L):
            for ent in selectedEnt: 
                ent.pos.x += 100 * dt
                    
       

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            for ent in selectedEnt: 
                ent.desiredSpeed = 0.0
        
        for ent in selectedEnt:
            #Metrics
            print 'heading:', ent.heading
            print 'desired heading:', ent.desiredHeading
            print 'max speed: ', ent.maxSpeed
            print 'desired speed: ', ent.desiredSpeed
            print 'speed: ', ent.speed
            #print str(ent.pos)
        
    def tick(self, dt):
        self.handleEntitiesController(dt)

    def stop(self):
        pass
