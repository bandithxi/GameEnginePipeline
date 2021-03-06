# Assignment 4

import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf

from ent import Renderable, Entity, EntityManager 

class ControlFrameListener(ogre.FrameListener):
    """To call the ent's tick and copy ent's new position to corresponding 
    scene node"""

    def __init__(self, entMgr):
        ogre.FrameListener.__init__(self)
        self.entMgr = entMgr

    def frameStarted(self, frameEvent):
        #print self.entMgr.count
        for ent in self.entMgr.list:
            ent.tick(frameEvent.timeSinceLastFrame)
        return True


 
class TutorialFrameListener(sf.FrameListener):
    """A FrameListener class that handles basic user input."""
 
    def __init__(self, renderWindow, camera, sceneManager, entMgr):
        # Subclass any Python-Ogre class and you must call its constructor.
        sf.FrameListener.__init__(self, renderWindow, camera)
        
        #As4, selects current element and show bounding
        self.entMgr = entMgr
        self.ent = entMgr.getSelected()
        self.ent.aspects[1].node.showBoundingBox(True)
        
            
        self.deltaVelocity = 10

        # Key and mouse state tracking.
        self.toggle = 0
        self.mouseDown = False
 
        # Populate the camera and scene manager containers.
        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
 
        # Set the rotation and movement speed.
        self.rotate = 0.13
        self.move = 250
 
    def frameStarted(self, frameEvent):

        # If the render window has been closed, end the program.
        if(self.renderWindow.isClosed()):
            return False
 
        # Capture and update each input device.
        self.Keyboard.capture()
        self.Mouse.capture()
 
        # Get the current mouse state.
        currMouse = self.Mouse.getMouseState()
 
        # Use the Left mouse button to turn Light1 on and off.         
        if currMouse.buttonDown(OIS.MB_Left) and not self.mouseDown:
            light = self.sceneManager.getLight('Light1')
            light.visible = not light.visible
 
        # Update the mouseDown boolean.            
        self.mouseDown = currMouse.buttonDown(OIS.MB_Left)
 
        # Update the toggle timer.
        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame
 
        # Swap the camera's viewpoint with the keys 1 or 2.
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_1):
            # Update the toggle timer.
            self.toggle = 0.1
            # Attach the camera to PitchNode1.
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode1")
            self.sceneManager.getSceneNode("PitchNode1").attachObject(self.camera)
 
        elif self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_2):
            # Update the toggle timer.
            self.toggle = 0.1
            # Attach the camera to PitchNode2.
            self.camera.parentSceneNode.detachObject(self.camera)
            self.camNode = self.sceneManager.getSceneNode("CamNode2")
            self.sceneManager.getSceneNode("PitchNode2").attachObject(self.camera)
 
        # Move the camera using keyboard input.
        transVector = ogre.Vector3(0, 0, 0)
        # Move Forward.
        if self.Keyboard.isKeyDown(OIS.KC_W):
           transVector.z -= self.move

        # Move Backward.
        if self.Keyboard.isKeyDown(OIS.KC_S):
            transVector.z += self.move

        # Strafe Left.
        if self.Keyboard.isKeyDown(OIS.KC_A):
            transVector.x -= self.move
      
        # Strafe Right.
        if self.Keyboard.isKeyDown(OIS.KC_D):
           transVector.x += self.move
       
        # Move Up.        
        if self.Keyboard.isKeyDown(OIS.KC_PGUP):
            transVector.y += self.move
       
        # Move Down.
        if self.Keyboard.isKeyDown(OIS.KC_PGDOWN):
            transVector.y -= self.move
        
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_TAB):
            self.toggle = 0.5
            self.ent.aspects[1].node.showBoundingBox(False)
            self.entMgr.next()
            self.ent = self.entMgr.getSelected()
            self.ent.aspects[1].node.showBoundingBox(True)

        # Yaw controls because sample framework won't allow Q/R usage
        if self.Keyboard.isKeyDown(OIS.KC_E):
            self.camNode.yaw(ogre.Degree(45) * frameEvent.timeSinceLastFrame)
 
        if self.Keyboard.isKeyDown(OIS.KC_T):
            self.camNode.yaw(ogre.Degree(-45) * frameEvent.timeSinceLastFrame)
  
         # Pitch controls, G up and H down 
        if self.Keyboard.isKeyDown(OIS.KC_G):
            self.camNode.pitch(ogre.Degree(45) * frameEvent.timeSinceLastFrame)
 
        if self.Keyboard.isKeyDown(OIS.KC_H):
            self.camNode.pitch(ogre.Degree(-45) * frameEvent.timeSinceLastFrame)
  
        # Translate the camera based on time.
        self.camNode.translate(self.camNode.orientation
                              * transVector
                              * frameEvent.timeSinceLastFrame)
 
        # Rotate the camera when the Right mouse button is down.
        if currMouse.buttonDown(OIS.MB_Right):
           self.camNode.yaw(ogre.Degree(-self.rotate 
                            * currMouse.X.rel).valueRadians())
           self.camNode.getChild(0).pitch(ogre.Degree(-self.rotate
                                          * currMouse.Y.rel).valueRadians())


        self.handleControls(frameEvent.timeSinceLastFrame)
 
        # If the escape key is pressed end the program.
        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)


    def handleControls(self, dtime):
        '''Needs to set ent's velocity based on keypres'''
        print 'heading:', self.ent.heading
        print 'desired heading:', self.ent.desiredHeading
        print 'max speed: ', self.ent.maxSpeed
        print 'desired speed: ', self.ent.desiredSpeed
        print 'speed: ', self.ent.speed

        # Increase Desired Speed
        if self.Keyboard.isKeyDown(OIS.KC_I):
            self.ent.desiredSpeed += 100 * dtime
            #print "Desired Speed:", self.ent.desiredSpeed  
           
        # Decrease Desired Heading
        if self.Keyboard.isKeyDown(OIS.KC_J):
            self.ent.desiredHeading -= 100 * dtime
            
            # Ensure we work with angles 0 to 360
            if self.ent.desiredHeading < 0:
                
                # Heading is also increase by 360 for simpler physics logic 
                self.ent.heading += 360
                self.ent.desiredHeading += 360  
            
        # Increase Desired Heading
        if self.Keyboard.isKeyDown(OIS.KC_L):
            self.ent.desiredHeading += 100 * dtime 
            
            # Ensure we work with angles 0 to 360
            if self.ent.desiredHeading > 360:
                
                # Heading is also decrease by 360 for simpler physics logic 
                self.ent.heading -= 360
                self.ent.desiredHeading -= 360  
            
            #move right

        if self.Keyboard.isKeyDown(OIS.KC_K):
            self.ent.desiredSpeed -= 100 * dtime
            #print "Desired Speed:", self.ent.desiredSpeed 
            
            #decreased desired speed

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.ent.desiredSpeed = 0
            

        return
 
class TutorialApplication(sf.Application):
    """The Application class."""
 
    def _createScene(self):
        self.entMgr = EntityManager()
        # Setup a scene with a high level of ambient light.
        sceneManager = self.sceneManager
        #sceneManager.ambientLight = 0.25, 0.25, 0.25
        #more light
        sceneManager.ambientLight = 1.0, 1.0, 1.0
 

        surfaceHeight = -100
        # Setup a ground plane at -100 height so the entire cube shows up
        plane = ogre.Plane ((0, 1, 0), surfaceHeight)
        meshManager = ogre.MeshManager.getSingleton ()
        #large plane 10000x10000
        meshManager.createPlane ('Ground', 'General', plane,
                                     10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        ent = sceneManager.createEntity('GroundEntity', 'Ground')
        sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('Examples/Water2')
        ent.castShadows = False
        #Like nice sky
        self.sceneManager.setSkyDome (True, "Examples/CloudySky", 5, 8)
        # Setup the first camera node and pitch node and aim it.
        camnode = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                               (0, 50, 500))
        #camnode.yaw(ogre.Degree(-45))

        node = camnode.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)

        # create game engine's entities from our as4 class (with small changes)
        
        #These are entities that are created with base class 'Entity'
        #For personal development
        #self.entMgr.createEntity("Cigarette", mesh = 'cigarette.mesh')
        #self.entMgr.createEntity("Boat0", mesh = '5086_Boat.mesh')
        #self.entMgr.createEntity("Boat1", mesh = 'boat.mesh')
        #self.entMgr.createEntity("CVN",  mesh = 'cvn68.mesh')
        #self.entMgr.createEntity("DDG",  mesh = 'ddg51.mesh')
        
        #self.entMgr.createEntity("Sail", mesh = 'sailboat.mesh')
        #self.entMgr.createEntity("Sleek", mesh = 'sleek.mesh')
    
        #self.entMgr.createEntity("Alien", mesh = 'alienship.mesh') 
        #self.entMgr.createEntity("Monterey", mesh = '3699_Monterey_189_92.mesh')
        #self.entMgr.createEntity("WaterCraft", mesh = '4685_Personal_Watercr.mesh')
        
        #self.entMgr.createEntity("Missile", mesh = 'missile.mesh')
        
        #This functions will create all 10 types of ships using 10 entity subclasses
        #For as4 requirement 
        self.entMgr.createDemo()

        #Round Robin to the first ship
        self.entMgr.next()
        offset = -1000

        for i in range(0, 11):
            self.curEnt = self.entMgr.getSelected()
            self.curEnt.pos = ogre.Vector3(offset, 0, 0)
           
            # create corresponding ogre ent
            self.pEnt = sceneManager.createEntity(self.curEnt.id, self.curEnt.mesh)
            self.pEnt.position = ogre.Vector3(offset, 0, 0)

            # create scene node to attach pEnt to
            self.curEntSceneNode = sceneManager.getRootSceneNode().createChildSceneNode(self.curEnt.id + 'node', ogre.Vector3(offset, 0, 0))
            self.curEntSceneNode.attachObject(self.pEnt)
            
            self.curEnt.aspects[1].attachNode(self.curEntSceneNode)
            
            self.entMgr.next()
            offset += 255
            
            #Lazy Hack to have all boats facing right
            if i == 9:
                self.curEntSceneNode.yaw(ogre.Degree(90))
                self.curEntSceneNode.scale(ogre.Vector3(.1,.1,.1))   
            elif i == 8:
                self.curEntSceneNode.yaw(ogre.Degree(90))
            elif i == 7:
                self.curEntSceneNode.scale(ogre.Vector3(10,10,10))
            elif i == 11:
                self.curEntSceneNode.scale(ogre.Vector3(15, 15, 15))
                
        # Setup the second camera node and pitch node.
        # don't need this
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode2', (0, 200, 400))
        node.createChildSceneNode('PitchNode2')        
 
    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.nearClipDistance = 5
 
    def _createFrameListener(self):
        self.frameListener = TutorialFrameListener(self.renderWindow,
                                                   self.camera,
                                                   self.sceneManager, 
                                                   self.entMgr)
        
        self.root.addFrameListener(self.frameListener)
        
        #add my ent frame listener
        self.controlFrameListener = ControlFrameListener(self.entMgr)
        self.root.addFrameListener(self.controlFrameListener)

        #self.frameListener.showDebugOverlay(True)
 
 
if __name__ == '__main__':
    try:
        ta = TutorialApplication()
        ta.go()
    except ogre.OgreException, e:
        print e
