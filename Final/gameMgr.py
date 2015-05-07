from vector import MyVector
import time
import AIaction as action

import ogre.renderer.OGRE as ogre


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

        self.gameTime = 600
        self.start = time.time()
       
        self.teamList = self.engine.entityMgr.entTypes
        self.chantList = self.engine.soundMgr.musicList
        self.p1Team = 0
        self.p2Team = 0
        
        self.teamSize = 5
        self.reset = False

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
        self.loadStad()
        
    def loadBall(self):
        self.engine.entityMgr.createEnt(self.engine.entityMgr.ballEnt, pos = MyVector(0, 0, 0))  

    def loadTeam1(self):
        x = 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = ogre.Vector3(x, 0, 0), team = 1)
        self.engine.entityMgr.selectedEntP1 = ent
        ent.node.showBoundingBox(True)
        
        x += 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = ogre.Vector3(x, 0, 600), team = 1)
        
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = ogre.Vector3(x, 0, -600), team = 1)
        x += 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = ogre.Vector3(x, 0, 0), team = 1)
        x += 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p1Team], pos = ogre.Vector3(x, 0, 0), team = 1)
        
        for en in self.engine.entityMgr.team1.values():
            en.desiredHeading = 180
            en.heading = 180
        
        
    def loadTeam2(self):
        x = -600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = ogre.Vector3(x, 0, 0), team = 2)
        self.engine.entityMgr.selectedEntP2 = ent
        ent.node.showBoundingBox(True)
       
        x -= 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = ogre.Vector3(x, 0, 600), team = 2)
        
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = ogre.Vector3(x, 0, -600), team = 2)
        x -= 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = ogre.Vector3(x, 0, 0), team = 2)
        x -= 600
        ent = self.engine.entityMgr.createEnt(self.teamList[self.p2Team], pos = ogre.Vector3(x, 0, 0), team = 2)
        

    def loadStad(self):
        self.engine.entityMgr.createStad()

    def tick(self, dt):
        self.updateTime() 
        
        if (self.startCheck):
            self.startCheck = False
            self.loadSetup()
            self.startGame()
            #print self.teamList[self.p1Team] , self.teamList[self.p2Team]
       
        if (self.reset):
            self.resetGame()
       
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
        self.gameTime = 600
        self.loadGameAsset()
        self.start = time.time()
        self.engine.guiMgr.overlay.hide()
        self.engine.guiMgr.hud2.show()
    
    def loadSetup(self):
        pass
    
    def gameOver(self):
        #self.backCheck = True
        pass

    def resetGame(self):
        self.reset = False
        for ent in self.engine.entityMgr.entities.values():
                    ent.aspects[2].clear()
                    ent.speed = 0
                    ent.desiredSpeed = 0

        for ent in self.engine.entityMgr.team1.values():
            self.engine.entityMgr.addAction(ent, action.GoHome(ent, ent.home))

        

        for ent in self.engine.entityMgr.team2.values():
            self.engine.entityMgr.addAction(ent, action.GoHome(ent, ent.home))
        


    
