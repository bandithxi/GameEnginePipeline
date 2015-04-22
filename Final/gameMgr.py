from vector import MyVector
# Dont Change

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        self.guiMgr = self.engine.guiMgr
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()
        self.mainMenu()

    def loadLevel(self):
        self.game()
    
    def mainMenu(self):
        self.guiMgr.displayMainMenu()
         
        ## Code to load sound here

    def game(self):
        x = 0
        
        for entType in self.engine.entityMgr.entTypes:
            print "*********************GameMgr Creating*********************" # , str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = MyVector(x, 0, 0))
            print "GameMgr Created: ", ent.uiname, ent.id
            x += 300

        self.engine.entityMgr.selectedEntities.append(ent)

    def tick(self, dt):
        pass

    def stop(self):
        pass
        
