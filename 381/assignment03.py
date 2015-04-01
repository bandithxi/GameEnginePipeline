import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf

class A3FrameListener(sf.FrameListener):
    
    def __init__(self, renderWindow, camera, sceneManager):
        sf.FrameListener.__init__(self, renderWindow, camera)
        self.velVector = (0, 0, 0)
 
        self.toggle = 0
        self.mouseDown = False
 
        self.camNode = camera.parentSceneNode.parentSceneNode
        self.sceneManager = sceneManager
        self.curEntNode = self.sceneManager.getSceneNode("CubeNode")

        self.entVelo = ogre.Vector3(0, 0, 0)
        self.rotate = 0.13
        self.move = 250
    
    def frameStarted(self, frameEvent):
    
        #send root message to turn off 
        if (self.renderWindow.isClosed()):
            return False
    
        self.Keyboard.capture()
	print "hello"
    
        camTransVector = ogre.Vector3(0, 0, 0)

        if self.Keyboard.isKeyDown(OIS.KC_W): 
            camTransVector.z -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_A): 
            camTransVector.x -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_S): 
            camTransVector.z += self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_D): 
            camTransVector.x += self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_F):
            camTransVector.y -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_E):
            camTransVector.y += self.move
 
        if self.Keyboard.isKeyDown(OIS.KC_UP):
            self.entVelo.z -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_DOWN):
            self.entVelo.z += self.move 
    
        if self.Keyboard.isKeyDown(OIS.KC_LEFT):
            self.entVelo.x -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_RIGHT):
            self.entVelo.x -= self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_PGUP):
            self.entVelo.y += self.move
    
        if self.Keyboard.isKeyDown(OIS.KC_PGDOWN): 
            self.entVelo.y -= self.move

        if self.Keyboard.isKeyDown(OIS.KC_SPACE):
            self.entVelo = ogre.Vector3(0, 0, 0)

        self.camNode.translate(self.camNode.orientation * transVector* frameEvent.timeSinceLastFrame)
 
        self.curEntNode.translate(self.curEntNode.orientation * self.entVelo * frameEvent.timeSinceLastFrame)

        return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)
 
        
class A3App(sf.Application):
    
    def _createScene(self):
        #initialize surface height
        self.surfaceHeight = 0
        
        #make the room slightly lit
        sceneManager = self.sceneManager
        sceneManager.ambientLight = (0.78, 0.89, 1)
        sceneManager.shadowTechnique = ogre.SHADOWTYPE_STENCIL_ADDITIVE

        #add cube that is able to cast shadow to scene
        ent = sceneManager.createEntity("Cube", "cube.mesh")
        ent.castShadows = True
        sceneManager.getRootSceneNode().createChildSceneNode("CubeNode").attachObject(ent)

        #create a plane and register it with mesh manager
        plane = ogre.Plane((0, 1, 0), self.surfaceHeight)
        meshManager = ogre.MeshManager.getSingleton()
        meshManager.createPlane("Ground", "General", plane, 10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
        
      
        #Ground plane 
        ent = sceneManager.createEntity("GroundEntity", "Ground")
        sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)
        #ent.setMaterialName("Examples/TextureEffect2")
        ent.setMaterialName("Examples/Rockwall")
        ent.castShadows = False
        
        node = sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                               (-400, 200, 400))
        node.yaw(ogre.Degree(-45))
        node = node.createChildSceneNode('PitchNode1')
        node.attachObject(self.camera)
 
        self.sceneManager.setSkyDome(True, "Examples/CloudySky", 5, 8)

        #point light and properties
        light = sceneManager.createLight("Sun")
        light.type = ogre.Light.LT_POINT
        light.position = (150, 300, 150)
        light.diffuseColour = (1, 1, 1)
        light.specularColour = (1, 1, 1)

    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('RTSCam')
        self.camera.position = (0,200, -1000)
        self.camera.lookAt ((0, 0, 0))
        self.camera.nearClipDistance = 5
         
    def _createFrameListener(self):
        self.frameListener = A3FrameListener(self.renderWindow, self.camera, self.sceneManager)
        self.root.addFrameListener(self.frameListener)
        self.frameListener.showDebugOverlay(True)
 

if __name__ == '__main__':
    app = A3App()
    app.go()
