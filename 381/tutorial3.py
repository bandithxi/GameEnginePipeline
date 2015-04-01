import ogre.renderer.OGRE as ogre
import SampleFramework as sf

class TuApp(sf.Application):

    def _createScene(self):
        fadeColour = (0.9, 0.9, 0.9)
        self.renderWindow.getViewport (0).backgroundColour = fadeColour
        self.sceneManager.setFog(ogre.FOG_LINEAR, fadeColour, 0, 50, 500)
        self.sceneManager.setWorldGeometry("terrain.cfg")
        #skybox best for space games
        #self.sceneManager.setSkyBox(True, "Examples/SpaceSkyBox", 5000, False)
        #skydome -> best for flying games
        #self.sceneManager.setSkyDome(True, "Examples/CloudySky", 5, 8)
        #skyplane -> best for games with valleys and high walls
        #plane = ogre.Plane((0, -1, 0), -1000)
        #self.sceneManager.setSkyPlane (True, plane, "Examples/SpaceSkyPlane", 1500, 75)
        #self.sceneManager.setSkyPlane (True, plane, "Examples/CloudySky", 1500, 40, True, 1.5, 150, 150)
    def _createCamera(self):
        self.camera = self.sceneManager.createCamera("RTSCam")
        self.camera.position = (750, 100, 500) 
        self.camera.lookAt((0, 0, 0))
        self.camera.nearClipDistance = 5
    
    def _chooseSceneManager(self):
        self.sceneManager = self.root.createSceneManager(ogre.ST_EXTERIOR_CLOSE,"TerrainSM")

   
        
 
if __name__ == "__main__":
    ta = TuApp()
    ta.go()
