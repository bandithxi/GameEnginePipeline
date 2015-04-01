from random import randrange
 
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import SampleFramework as sf
 
 
class Character(object):
 
    def __init__(self):
        pass
 
    def update(self, elapsedTime, input):
        pass
 
    def getSightNode(self):
        return self.sightNode
 
    def getCameraNode(self):
        return self.cameraNode
 
    def getWorldPosition(self):
        return self.mainNode.getWorldPosition()
 
class OgreCharacter(Character):
 
    def __init__(self, name, sceneManager):
        self.name = name
        self.sceneManager = sceneManager
        self.mainNode = self.sceneManager.getRootSceneNode() \
                                            .createChildSceneNode(self.name)
        self.sightNode = self.mainNode.createChildSceneNode(self.name
                                                            + "_sight",
                                                            (0, 0, 100))
        self.cameraNode = self.mainNode.createChildSceneNode(self.name
                                                            + "_camera",
                                                            (0, 50, -100))
 
        self.entity = self.sceneManager.createEntity(self.name,
                                                        "OgreHead.mesh")
        self.mainNode.attachObject(self.entity)
 
    def __del__(self):
        self.mainNode.detachAllObjects()
        del self.entity
        self.mainNode.removeAndDestroyAllChildren()
        self.sceneManager.destroySceneNode(self.name)
 
    def update(self, elapsedTime, input):
        if input.isKeyDown(OIS.KC_W):
            self.mainNode.translate(self.mainNode.getOrientation()
                                        * (0, 0, 100 * elapsedTime))
        if input.isKeyDown(OIS.KC_S):
            self.mainNode.translate(self.mainNode.getOrientation()
                                        * (0, 0, -50 * elapsedTime))
        if input.isKeyDown(OIS.KC_A):
            self.mainNode.yaw(ogre.Radian(2 * elapsedTime))
        if input.isKeyDown(OIS.KC_D):
            self.mainNode.yaw(ogre.Radian(-2 * elapsedTime))
 
    def setVisible(self, visible):
        self.mainNode.setVisible(visible)
 
class ExtendedCamera():
    def __init__(self, name, sceneManager, camera = None):
            self.name = name
            self.sceneManager = sceneManager
            self.cameraNode = self.sceneManager.getRootSceneNode() \
                                                .createChildSceneNode(self.name)
            self.targetNode = self.sceneManager.getRootSceneNode() \
                                                .createChildSceneNode(self.name
                                                                      + "_target")
            self.cameraNode.setAutoTracking(True, self.targetNode)
            self.cameraNode.setFixedYawAxis(True)
 
            if not camera:
                self.camera = self.sceneManager.createCamera(self.name)
                self.ownCamera = True
            else:
                self.camera = camera
                self.camera.setPosition(0,0,0)
                self.ownCamera = False
 
            self.cameraNode.attachObject(self.camera)
            self.tightness = 0.1
 
    def __del__(self):
            self.cameraNode.detachAllObjects()
            if self.ownCamera:
                del self.camera
            self.sceneManager.destroySceneNode(self.name)
            self.sceneManager.destroySceneNode(self.name + "_target")
 
    def getCameraPosition(self):
        return self.cameraNode.getPosition()
 
    def instantUpdate(self, cameraPosition, targetPosition):
        self.cameraNode.setPosition(cameraPosition)
        self.targetNode.setPosition(targetPosition)
 
    def update(self, elapsedTime, cameraPosition, targetPosition):
        displacement = (ogre.Vector3(cameraPosition) - self.cameraNode \
                                                        .getPosition()) \
                                                        * self.tightness
        self.cameraNode.translate(displacement)
 
        displacement = (ogre.Vector3(targetPosition) - self.targetNode \
                                                        .getPosition()) \
                                                        * self.tightness
        self.targetNode.translate(displacement)
 
class SampleListener(sf.FrameListener):
 
    def __init__(self, renderWindow, camera):
        super(SampleListener, self).__init__(renderWindow, camera)
        self.char = 0
        self.exCamera = 0
        self.mode = 0
 
    def setCharacter(self, character):
        self.char = character
 
    def setExtendedCamera(self, cam):
        self.exCamera = cam
 
    def frameStarted(self, evt):
        self.Keyboard.capture()
 
        if self.char:
            self.char.update(evt.timeSinceLastFrame, self.Keyboard)
 
            if self.exCamera:
                # could use a switch proxy here, but couldn't be bothered
                if self.mode == 0:
                    self.exCamera.update(evt.timeSinceLastFrame,
                                         self.char.getCameraNode() \
                                                .getWorldPosition(),
                                         self.char.getSightNode() \
                                                .getWorldPosition())
                elif self.mode == 1:
                    self.exCamera.update(evt.timeSinceLastFrame,
                                         (0, 200, 0),
                                         self.char.getSightNode() \
                                                .getWorldPosition())
                elif self.mode == 2:
                    self.exCamera.update(evt.timeSinceLastFrame,
                                         self.char.getWorldPosition(),
                                         self.char.getSightNode() \
                                                .getWorldPosition())
 
        if self.Keyboard.isKeyDown(OIS.KC_F1):
            self.mode = 0
            if self.char:
                self.char.setVisible(True)
            if self.exCamera:
                if self.char:
                    self.exCamera.instantUpdate(self.char.getCameraNode() \
                                                         .getWorldPosition(),
                                                self.char.getSightNode() \
                                                         .getWorldPosition())
                self.exCamera.tightness = 0.01
 
        if self.Keyboard.isKeyDown(OIS.KC_F2):
            self.mode = 1
            if self.char:
                self.char.setVisible(True)
            if self.exCamera:
                if self.char:
                    self.exCamera.instantUpdate((0, 200, 0),
                                                self.char.getSightNode() \
                                                        .getWorldPosition())
                self.exCamera.tightness = 0.01
 
        if self.Keyboard.isKeyDown(OIS.KC_F3):
            self.mode = 2
            if self.char:
                self.char.setVisible(False)
            if self.exCamera:
                if self.char:
                    self.exCamera.instantUpdate(self.char.getWorldPosition(),
                                               self.char.getSightNode() \
                                                        .getWorldPosition())
                self.exCamera.tightness = 1.0
 
        if self.Keyboard.isKeyDown(OIS.KC_ESCAPE):
            return False
 
        return True
 
class TestApp(sf.Application):
 
    def _createScene(self):
        self.sceneManager.setAmbientLight((0.2, 0.2, 0.2))
 
        light = self.sceneManager.createLight("MainLight")
        light.setType(ogre.Light.LT_DIRECTIONAL)
        light.setDirection(-0.5, -0.5, 0)
 
        self.camera.setPosition(0, 0, 0)
 
        for i in range(30):
            knotNode = self.sceneManager.getRootSceneNode() \
                                            .createChildSceneNode(str(i),
                                                (randrange(-1000, 1000),
                                                 0,
                                                 randrange(-1000, 1000)
                                                ))
            knotEntity = self.sceneManager.createEntity(str(i), "knot.mesh")
            knotNode.attachObject(knotEntity)
 
        ogreChar = OgreCharacter("Ogre 1", self.sceneManager)
        exCamera = ExtendedCamera("ExtendedCamera", self.sceneManager,
                                    self.camera)
 
        self.frameListener = SampleListener(self.renderWindow, self.camera)
        self.frameListener.setCharacter(ogreChar)
        self.frameListener.setExtendedCamera(exCamera)
 
    def _createFrameListener(self):
        self.frameListner = SampleListener(self.renderWindow, self.camera)
        self.root.addFrameListener(self.frameListener)
 
if __name__ == '__main__':
    app = TestApp()
    app.go()
