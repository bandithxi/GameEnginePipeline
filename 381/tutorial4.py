import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf
 
 
class A3FrameListener(sf.FrameListener):
    """A FrameListener class that handles basic user input."""
 
    def __init__(self, renderWindow, camera, sceneManager):
        # Subclass any Python-Ogre class and you must call its constructor.
        sf.FrameListener.__init__(self, renderWindow, camera)
 
        # Key and mouse state tracking.
        self.toggle = 0
        self.mouseDown = False
 
        # Populate the camera and scene manager containers.
        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
        self.entCtr = 0

        self.curEntNode = self.sceneManager.getSceneNode("CubeNode" + str(self.entCtr))

        self.entVelo = ogre.Vector3(0, 0, 0)
        
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
        if self.Keyboard.isKeyDown(OIS.KC_F):
            transVector.y -= self.move
        # Move Down.
        if self.Keyboard.isKeyDown(OIS.KC_E):
            transVector.y += self.move
        
        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8):
            self.entVelo.z -= 1 

        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD2):
            self.entVelo.z += 1 
    
        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD4):
            self.entVelo.x -= 1
    
        if self.Keyboard.isKeyDown(OIS.KC_NUMPAD6):
            self.entVelo.x += 1
    
        if self.Keyboard.isKeyDown(OIS.KC_PGUP):
            self.entVelo.y += 1
    
        if self.Keyboard.isKeyDown(OIS.KC_PGDOWN): 
            self.entVelo.y -= 1

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.entVelo = ogre.Vector3(0, 0, 0)

        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame
 
        if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_TAB):
            self.toggle = 0.1
            self.entCtr += 1
            
            if self.entCtr > 1:
                self.entCtr = 0
            self.curEntNode = self.sceneManager.getSceneNode("CubeNode" + str(self.entCtr))
          
        self.curEntNode.translate(self.curEntNode.orientation * self.entVelo * frameEvent.timeSinceLastFrame)

        # Translate the camera based on time.
        self.camNode.translate(self.camNode.orientation
                              * transVector
                              * frameEvent.timeSinceLastFrame)
 
        # If the escape key is pressed end the program.
        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)
 
class A3App(sf.Application):
    """The Application class."""
 
    def _createScene(self):
        
        self.surfaceHeight = 0

        # Setup a scene with a low level of ambient light.
        sceneManager = self.sceneManager
        sceneManager.ambientLight = (0.78, 0.89, 1)
        sceneManager.shadowTechnique = ogre.SHADOWTYPE_STENCIL_ADDITIVE

        # Setup a mesh entity and attach it to a scene node.
        entity = sceneManager.createEntity('Cube0', 'cube.mesh')
        node = sceneManager.getRootSceneNode().createChildSceneNode('CubeNode0', (0, 0, 0))
        node.attachObject(entity)
        
        entity = sceneManager.createEntity('Cube1', 'cube.mesh')
        node = sceneManager.getRootSceneNode().createChildSceneNode('CubeNode1', (100, 200, 0))
        node.attachObject(entity)
 
        plane = ogre.Plane((0, 1, 0), self.surfaceHeight)
        meshManager = ogre.MeshManager.getSingleton()
        meshManager.createPlane("Ground", "General", plane, 10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        
        ent = sceneManager.createEntity("GroundEntity", "Ground")
        sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)
        ent.setMaterialName("Examples/TextureEffect2")
        #ent.setMaterialName("Examples/Rockwall")
        ent.castShadows = False
        
        self.sceneManager.setSkyDome(True, "Examples/CloudySky", 5, 8)

        # Setup a White point light.
        light = sceneManager.createLight('Light1')
        light.type = ogre.Light.LT_POINT
        light.position = (150, 300, 150)
        light.diffuseColour = (1, 1, 1)
        light.specularColour = (1, 1, 1)
 
        # Setup the first camera node and pitch node and aim it.
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                               (-400, 200, 400))
        node.yaw(ogre.Degree(-45))
        node = node.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)
 
        # Setup the second camera node and pitch node.
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode2',
                                                              (0, 200, 400))
        node.createChildSceneNode('PitchNode2')        
 
    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.nearClipDistance = 5
 
    def _createFrameListener(self):
        self.frameListener = A3FrameListener(self.renderWindow,
                                                   self.camera,
                                                   self.sceneManager)
        self.root.addFrameListener(self.frameListener)
        self.frameListener.showDebugOverlay(True)
 
 
if __name__ == '__main__':
    try:
        ta = A3App()
        ta.go()
    except ogre.OgreException, e:
        print e


