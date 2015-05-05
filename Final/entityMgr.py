import ent
from vector import MyVector

class EntityMgr:
    def __init__(self, engine):
        #print "__init__ EntityMgr"
        self.engine = engine

    def init(self):
        self.entities = {}
        self.nEnts = 0

        self.selectedEntP1 = None
        self.selectedEntP2 = None

        self.selectedEnt = None
        
        self.selectedEntIndex = 0
        self.selectedEntIndexP1 = -1
        self.selectedEntIndexP2 = -1
        self.team1 = {}
        self.team2 = {}
        self.nP1 = 0
        self.nP2 = 0
        self.selectedEntities = []

        self.entTypes = [ent.Liverpool, ent.BVB, ent.Arsenal, ent.Chelsea, ent.EgbertTeam]
        self.ball = ent.Ball
        self.stands = ent.Stands
        self.top = ent.TopStad
        self.lowWall = ent.lowWall
        self.stadiumParts = [ent.Stands, ent.TopStad, ent.lowWall, ent.Entrance, ent.highWall, ent.midWall, ent.post, ent.RoofFrame, ent.stairs ]

    def createEnt(self, entType, pos = MyVector(0,0,0), yaw = 0, team = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, yaw = yaw)
        ent.init()
  
        self.entities[self.nEnts] = ent
        self.selectedEnt = ent
        self.selectedEntIndex = self.nEnts;
        
        self.nEnts = self.nEnts+1        
        
        if (team == 1):
            print ent
            self.team1[self.nP1] = ent 
            self.nP1 +=1
        elif (team == 2): 
            self.team2[self.nP2] = ent
            self.nP2 +=1 
        return ent
    
    def createStad(self):
        for entType in self.stadiumParts:
         
            ent = self.createEnt(entType)
            

    def getNextEnt(self, team):
        if (team == 1):
            if self.selectedEntIndexP1 >= self.nP1 - 1:
                self.selectedEntIndexP1 = 0
            else:
                self.selectedEntIndexP1 += 1
        
           # print self.team1
            self.selectedEntP1 = self.team1[self.selectedEntIndexP1]
            #print "EntMgr selected: ", str(self.selectedEnt)
            return self.selectedEntP1
        else:
            if self.selectedEntIndexP2 >= self.nP2 - 1:
                self.selectedEntIndexP2 = 0
            else:
                self.selectedEntIndexP2 += 1
        
            print self.team2
            self.selectedEntP2 = self.team2[self.selectedEntIndexP2]
            #print "EntMgr selected: ", str(self.selectedEnt)
            return self.selectedEntP2


    def getSelected(self, team):
        if (team == 1):
            return self.selectedEntP1
        else:
            return self.selectedEntP2

    def tick(self, dt):
        for eid, entity in self.entities.iteritems():
            entity.tick(dt)
