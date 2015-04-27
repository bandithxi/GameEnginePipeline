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
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()
        self.mainMenu()

    def loadLevel(self):
        self.game()
    
    def mainMenu(self):
        self.guiMgr.displayMainMenu()
        self.guiMgr.displayHud()
         
        ## Code to load sound here

    def game(self):
        self.gameTime = 300
        self.start = time.time()

        x = -300
        
        for entType in self.engine.entityMgr.entTypes:
            print "*********************GameMgr Creating*********************" # , str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = MyVector(x, 0, 0))
            print "GameMgr Created: ", ent.uiname, ent.id
            x += 300

        
    def tick(self, dt):
        self.updateTime()
        
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

    
     

