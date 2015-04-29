from vector import MyVector
import time
# Dont Change

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        self.guiMgr = self.engine.guiMgr
        self.sfxMgr = self.engine.soundMgr
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
       
        self.teamList = self.engine.entityMgr.entTypes
        self.chantList = self.engine.soundMgr.musicList
        self.p1Team = 0
        self.p2Team = 0
        
        self.teamSize = 1

        print "starting Game mgr"
        pass

    def init(self):
        self.guiMgr.createMainMenu()
        self.guiMgr.createHud()
        self.sfxMgr.playMusic("Champions_League_theme")
        #self.sfxMgr.playMusic("bvb")
        #self.sfxMgr.playMusic("liverpool")
        #self.sfxMgr.playMusic("arsenal")

    def loadLevel(self):
        pass
    
    def mainMenu(self):
        pass
        ## Code to load sound here

    def loadGameAsset(self):
        self.loadTeam1()
        self.loadTeam2()
        self.loadBall()
        
    def loadBall(self):
        self.engine.entityMgr.createEnt(self.engine.entityMgr.ball, pos = MyVector(0, 0, 0))  

    def loadTeam1(self):
        x = 300
        for i in range(self.teamSize):
            ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = MyVector(x, 0, 0))
            x += 300
    
    def loadTeam2(self):
        x = -300
        for i in range(self.teamSize):
            ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = MyVector(x, 0, 0))
            x -= 300

    def tick(self, dt):
        self.updateTime() 
        
        if (self.startCheck):
            self.startCheck = False
            self.loadSetup()
            self.startGame()
            #print self.teamList[self.p1Team] , self.teamList[self.p2Team]
        pass

    def stop(self):
        pass
 

    def updateTime(self):
        self.end = time.time()
        #print self.backCheck
        if (self.end - self.start) > 1 :
            #print (self.end - self.start) 
            self.start = self.end
            self.gameTime-=1
            #print self.gameTime

    
    def startGame(self):
        self.sfxMgr.stopMusic("Champions_League_theme")
        self.sfxMgr.playMusic(self.chantList[self.p1Team])
        self.gameTime = 300
        self.loadGameAsset()
        self.start = time.time()
        self.engine.guiMgr.overlay.hide()
        self.engine.guiMgr.hud2.show()

    
    def loadSetup(self):
        pass
    
    def gameOver(self):
        #self.backCheck = True
        pass
