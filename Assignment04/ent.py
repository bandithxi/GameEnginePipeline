# Entity class to hold information about entities for 38Engine

#from vector import MyVector
import ogre.renderer.OGRE as ogre
from physics import Physics

class Renderable:

    def __init__(self, ent):
        self.ent = ent
        self.node = None
        
 
    def tick(self, dtime):
       # if self.node is not None:
        self.node.position = self.ent.pos
        self.node.resetOrientation()
        self.node.yaw(ogre.Degree(self.ent.heading))
            #self.node.yaw(ogre.Degree(45))

        #print self.ent.heading
        #print self.ent.desiredHeading

    def attachNode(self, node):
        self.node = node

class Entity:
    
    def __init__(self, id = 'Entity', pos = ogre.Vector3(0,0,0), mesh = 'robot.mesh', vel = ogre.Vector3(0, 0, 0), yaw = 0, spd = 0, heading = 0, desSpd = 0, desHead = 0, acc = 5, tRate = 20, maxSpeed = 5):
        self.id = id
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.yaw = yaw
        
        self.aspects = []
        self.aspectTypes = [Physics, Renderable]
    
        
        self.deltaSpeed = 10
        
        #added for assignment 4
        self.speed = spd
        self.heading = heading
        self.desiredSpeed = desSpd
        self.desiredHeading = desHead
        
        #must be something other than 0 or we can't move
        self.acceleration = acc
        self.turningRate = tRate
        self.deltaHeading = 0
        self.initAspects()
       
        self.maxSpeed = maxSpeed

    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))
        

    def tick(self, dtime):
        #print "Ent tick", str(self.vel)
        for aspect in self.aspects:
            aspect.tick(dtime)


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s, yaw: %f" % (self.id, str(self.pos), str(self.vel), self.yaw)
        return x

#simple entity manager that only allows selections of one entity and no deletion 
class EntityManager:
    id = 0

    def __init__(self):
        self.list = []
        self.count = 0
        self.select = 0

    def createEntity(self, name = None,  mesh = None):
        
        #unique id, if none is provided
        if name is None:
            name = 'emID' + str(id)
            self.__class__.id += 1 
        
        self.list.append(Entity(id = name, mesh = mesh))
        
        self.select = self.count
         
        self.count += 1
        
    def getSelected(self):
        return self.list[self.select]
    
    def next(self):
        self.select += 1
        
        if self.select >= self.count:
            self.select = 0

    def createDemo(self):
        
        ent = SpeedBoatEntity()
        self.addEntity(ent)
        
        ent = BoatEntity()
        self.addEntity(ent)
        
        ent = FisherEntity()
        self.addEntity(ent)
        
        ent = CarrierEntity('Nimitz')
        self.addEntity(ent)
        
        ent = DestroyerEntity()
        self.addEntity(ent)
        
        ent = SailEntity('old')
        self.addEntity(ent)
        
        ent = SleekEntity()
        self.addEntity(ent)
        
        ent = AlienShipEntity('Scimitar')
        self.addEntity(ent)
        
        ent = MontereyEntity()
        self.addEntity(ent)
        
        ent = JetSkiEntity('See-Doo')
        self.addEntity(ent)
        
        ent = missileEntity()
        self.addEntity(ent)

    #not required for as4 and minimally tested
    def addEntity(self, ent):
        self.list.append(ent)
        self.select = self.count
        self.count += 1

class missileEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'missile' + str(id), mesh = 'missile.mesh', acc = 50, tRate = 100, maxSpeed = 1000)
        self.__class__.id += 1

class JetSkiEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Jet Ski' + str(id), mesh = '4685_Personal_Watercr.mesh', acc = 10, tRate = 35, maxSpeed = 40)
        self.__class__.id += 1

class CarrierEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Carrier' + str(id), mesh = 'cvn68.mesh', acc = 5, tRate = 5, maxSpeed = 250)
        self.__class__.id += 1

class SailEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Lady' + str(id), mesh = 'sailboat.mesh', acc = 2, tRate = 25, maxSpeed = 36)
        self.__class__.id += 1

class AlienShipEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, 'Star Ship' + name + str(id), mesh = 'alienship.mesh', acc = 150, tRate = 25, maxSpeed = 700)
        self.__class__.id += 1

class MontereyEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Monterey' + str(id), mesh = '3699_Monterey_189_92.mesh', acc = 7, tRate = 35, maxSpeed = 60)
        self.__class__.id += 1

class SleekEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Sleek' + str(id), mesh = 'sleek.mesh', acc = 12, tRate = 12, maxSpeed = 120)
        self.__class__.id += 1

class DestroyerEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Destroyer' + str(id), mesh = 'ddg51.mesh', acc = 7, tRate = 15, maxSpeed = 150)
        self.__class__.id += 1

class BoatEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Boat' + str(id), mesh = 'boat.mesh', acc = 30, tRate = 30, maxSpeed = 55)
        self.__class__.id += 1

class FisherEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Fishing Boat' + str(id), mesh = '5086_Boat.mesh', acc = 10, tRate = 30, maxSpeed = 50)
        self.__class__.id += 1

class SpeedBoatEntity(Entity):
    id = 0

    def __init__(self, name = ''):        
        Entity.__init__(self, name + 'Speed Boat' + str(id), mesh = 'cigarette.mesh', acc = 30, tRate = 45, maxSpeed = 150)
        self.__class__.id += 1

