import math
from vector import MyVector
from physics import Physics

class Entity:
    def __init__(self, name = 'untiled', pos = MyVector(0, 0, 0), vel = MyVector(0, 0, 0), mesh = 'untiled.mesh', yaw = 0):
        self.name = name
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.yaw = yaw
        self.aspectTypes = ['Physics']
        self.aspects = [Physics(self)]

    def __str__(self):
        return str(self.name) + ' ' + str(self.pos) + ' ' + str(self.vel) + ' ' + str(self.mesh) + ' ' + str(self.yaw)

    def tick(self, dtime):
        for asp in self.aspects:
            asp.update(dtime)
 
print "Entity test cases"
x = Entity("Entity1")
print str(x)

x = Entity("Tank4", pos = MyVector(100, 0, 100))
print str(x)

x = Entity("Bubble9", vel = MyVector(1, 0, 0))
print str(x)

x = Entity("x3", mesh = 'robot.mesh')
print str(x)

x = Entity("Robot1", yaw = math.pi/2.0)
print str(x) + '\n'
