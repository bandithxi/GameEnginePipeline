from vector import MyVector
import time
# Dont Change

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        self.guiMgr = self.engine.guiMgr
        self.half = 1
        self.scoreOne = 0
        self.scoreTwo = 0
        self.startCheck = False
        self.instructionsCheck = False
        self.creditsCheck = False
        self.backCheck = False
        self.teamCheck = False

        self.gameTime = 300
        self.start = time.time()
        print "starting Game mgr"
        pass

    def init(self):
        self.guiMgr.createMainMenu()
        self.guiMgr.createHud()

    def loadLevel(self):
        pass
    
    def mainMenu(self):
        pass
        ## Code to load sound here

    def loadGameAsset(self):

        x = -300
        
        for entType in self.engine.entityMgr.entTypes:
            print "*********************GameMgr Creating*********************" # , str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = MyVector(x, 0, 0))
            print "GameMgr Created: ", ent.uiname, ent.id
            x += 300

        
    def tick(self, dt):
        self.updateTime() 
        
        if (self.startCheck):
            self.startCheck = False
            self.loadSetup()
            self.startGame()
        pass

    def stop(self):
        pass
 

    def updateTime(self):
        self.end = time.time()

        if (self.end - self.start) > 1 :
            #print (self.end - self.start) 
            self.start = self.end
            self.gameTime-=1

            #print self.gameTime

    
    def startGame(self):
        self.gameTime = 300
        self.loadGameAsset()
        self.start = time.time()
        self.engine.guiMgr.overlay.hide()
        self.engine.guiMgr.hud2.show()

    
    def loadSetup(self):
        pass
