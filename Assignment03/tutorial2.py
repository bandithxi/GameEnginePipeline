import ogre.renderer.OGRE as ogre
import SampleFramework as sf

class TutorialApp(sf.Application):
    def _createScene(self):
        sceneManager = self.sceneManager
        sceneManager.ambientLight = (0, 0, 0)
        sceneManager.shadowTechnique = ogre.SHADOWTYPE_STENCIL_ADDITIVE

        ent = sceneManager.createEntity("Ninja", "ninja.mesh")
        ent.castShadows = True
        sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)

        plane = ogre.Plane((0, 1, 0), 0)
        meshManager = ogre.MeshManager.getSingleton()
        meshManager.createPlane("Ground", "General", plane, 1500, 1500, 20, 20, True, 1, 5, 5, (0, 0, 1))
        
        ent = sceneManager.createEntity("GroundEntity", "Ground")
        sceneManager.getRootSceneNode().createChildSceneNode().attachObject(ent)
        ent.setMaterialName("Examples/Rockwall")
        ent.castShadows = False

        #point light and properties
        light = sceneManager.createLight("PointLight")
        light.type = ogre.Light.LT_POINT
        light.position = (150, 300, 150)
        light.diffuseColour = (.5, .0, .0)
        light.specularColour = (.5, .0, .0)

        #directional light and properties
        light = sceneManager.createLight("DirectionalLight")
        light.type = ogre.Light.LT_DIRECTIONAL
        light.diffuseColour = (.5, .5, .0)
        light.specularColour = (.75, .75, .75)
        light.direction = (0, -1, 1)

        #spot light and properties
        light = sceneManager.createLight("spotLight")
        light.type = ogre.Light.LT_SPOTLIGHT
        light.diffuseColour = (0, 0, .5)
        light.specularColour = (0, 0, .5)
        light.direction = (-1, -1, 0)
        light.position = (300, 300, 0)
        light.setSpotlightRange(ogre.Degree(35), ogre.Degree(50))

    def _createCamera(self):
        self.camera = self.sceneManager.createCamera('PlayerCam')
        self.camera.position = (0,150, -500)
        self.camera.lookAt ((0, 0, 0))
        self.camera.nearClipDistance = 5
        
    def _createViewports(self):
       viewport = self.renderWindow.addViewport(self.camera)
       viewport.backGroundColor = (0, 0, 0)
       self.camera.aspectRation = float (viewport.actualWidth) / float (viewport.actualHeight)

if __name__ == '__main__':
    ta = TutorialApp()
    ta.go()
