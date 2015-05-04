import ent
from vector import MyVector

class EntityMgr:
    def __init__(self, engine):
        #print "__init__ EntityMgr"
        self.engine = engine

    def init(self):
        self.entities = {}
        self.nEnts = 0

        self.selectedEnt = None
        self.selectedEntIndex = 0
        self.selectedEntities = []

        self.entTypes = [ent.Liverpool, ent.BVB, ent.Arsenal, ent.Chelsea, ent.EgbertTeam]
        self.ball = ent.Ball
        self.stands = ent.Stands
        self.top = ent.TopStad
        self.lowWall = ent.lowWall
        self.stadiumParts = [ent.Stands, ent.TopStad, ent.lowWall, ent.Entrance, ent.highWall, ent.midWall, ent.post, ent.RoofFrame, ent.stairs ]

    def createEnt(self, entType, pos = MyVector(0,0,0), yaw = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, yaw = yaw)
        ent.init()
  
        self.entities[self.nEnts] = ent
        self.selectedEnt = ent
        self.selectedEntIndex = self.nEnts;

        #changed
        #ent.setMaterialName(ent.material) d

        self.nEnts = self.nEnts+1        
        return ent
    
    def createStad(self):
        for entType in self.stadiumParts:
         
            ent = self.createEnt(entType)
            #ent.setMaterial

    def getNextEnt(self):
        if self.selectedEntIndex >= self.nEnts - 1:
            self.selectedEntIndex = 0
        else:
            self.selectedEntIndex += 1

        self.selectedEnt = self.entities[self.selectedEntIndex]
        #print "EntMgr selected: ", str(self.selectedEnt)
        return self.selectedEnt

    def getSelected(self):
        return self.selectedEnt

    def tick(self, dt):
        for eid, entity in self.entities.iteritems():
            entity.tick(dt)
