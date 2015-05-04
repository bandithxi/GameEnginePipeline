# Entity class to hold information about entities for 38Engine
# Daniel Sanchez

import ogre.renderer.OGRE as ogre
from physics import Physics
from renderer import Renderer
from vector import MyVector
# import math
# import time


class Entity:
    def __init__(self, engine, id, pos = MyVector(0,0,0), mesh = 'robot.mesh', 
                                  vel = MyVector(0,0,0), yaw = 0):
        self.engine = engine
        self.id = id
        self.pos = pos
        self.vel = ogre.Vector3(0, 0, 0)
        self.mesh = mesh
        self.node  = None
        self.yaw = 0
        self.deltaSpeed = 5
        self.deltaYaw = 0.0
        self.speed = 0.0
        self.heading = 0.0
        self.aspectTypes = [Physics, Renderer]
        self.aspects = []
        self.scale = ogre.Vector3(1, 1, 1)
        self.wakeSize = 'Small'
        self.hasAnimation = False

        #Make jet ski face the same way
        self.offset = 0

    def init(self):
        self.initAspects()


    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))

    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s, yaw: %f" % (self.id, str(self.pos), str(self.vel), self.yaw)
        return x


class Ball(Entity):
    def __init__(self, engine, id, pos = MyVector(0,0,0), vel = MyVector(0,0,0), yaw = 0):
        Entity.__init__(self, engine, id, pos = MyVector(0,25,0), vel = vel, yaw = yaw) 
        
        self.mesh = 'sphere.mesh'
        self.uiname = 'Ball'
        self.acceleration = 250
        self.turningRate = 30
        self.maxSpeed = 1000
        self.desiredSpeed = 0
        self.desiredHeading = 90
        self.speed = 0
        self.heading = 90    
        self.wakeSize = 'Large'
        self.scale = ogre.Vector3(.5, .5, .5)
        self.wakeSize = 'Large'
        self.pitch = 0.0
        self.spin = 0.0
        self.attachEnt = None
        self.toggle = 0.0
        


class PlayerA(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = 'ninja.mesh'
        self.uiname = 'playerA' + str(PlayerA.id)
        PlayerA.id += 1
        self.acceleration = 360
        self.turningRate = 120
        self.maxSpeed = 400
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(-90)
        self.hasAnimation = True
        self.scale = ogre.Vector3(.5, .5, .5)
        #changed
        self.material = "Examples/EgbertTeam"
   
class PlayerB(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = 'ninja.mesh'
        self.uiname = 'playerB' + str(PlayerB.id)
        PlayerB.id += 1
        self.acceleration = 360
        self.turningRate = 120
        self.maxSpeed = 400
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(180)
        self.hasAnimation = True
        self.scale = ogre.Vector3(2, 2, 2)


class TopStad(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = 'WireFrameTopStad.mesh'
        self.uiname = 'Top'
        PlayerB.id += 1
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)

class Stands(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "Stands.mesh"
        self.uiname = 'Stands'
        PlayerB.id += 1
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)

class Entrance(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "entrance.mesh"
        self.uiname = 'entrance'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)

class highWall(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "highWall.mesh"
        self.uiname = 'highWall'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)

class lowWall(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "lowWall.mesh"
        self.uiname = 'lowWall'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)

class midWall(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "midWall.mesh"
        self.uiname = 'midWall'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)


class post(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "post.mesh"
        self.uiname = 'post'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)


class RoofFrame(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "RoofFrame.mesh"
        self.uiname = 'RoofFrame'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)


class stairs(Entity):
    id = 0
    def __init__(self, engine, id, pos = MyVector(0, 0 ,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        print "player init"
        self.mesh = "stairs.mesh"
        self.uiname = 'stairs'
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.wakeSize = 'Large'
        self.offset = ogre.Degree(90)
        
        #self.scale = ogre.Vector3(1, 1, 1)

        self.scale = ogre.Vector3(50, 50, 50)
