import ogre.io.OIS as OIS
    
class SelectionMgr:

    def __init__(self, engine):
        self.engine = engine

    def init(self):
        self.keyboard = self.engine.inputMgr.keyboard
        self.toggle = 0.1

        # buttonPositions
        self.buttonStartX = self.engine.guiMgr.buttonStartX
        self.buttonStartY = self.engine.guiMgr.buttonStartY
        self.buttonInstructY = self.engine.guiMgr.buttonInstructY
        self.buttonCreditsY = self.engine.guiMgr.buttonCreditsY
        self.buttonTeamSelectionY = self.engine.guiMgr.buttonTeamSelectionY
        
        #changed 
        self.windowWidth  = self.engine.gfxMgr.renderWindow.getWidth()
        self.windowHeight = self.engine.gfxMgr.renderWindow.getHeight()

    def tick(self, dt):
        if self.toggle >=0:
            self.toggle -= dt
        selectedEntIndex = self.engine.entityMgr.selectedEntIndex
        #print "selected: ", str(selectedEntIndex)

        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
            self.toggle = 0.4
            #print "tab test"

            if self.keyboard.isKeyDown(OIS.KC_LSHIFT):
                self.addNextEnt()
            else:
                self.selectNextEnt()

            # ent = self.engine.entityMgr.selectedEnt
            # ent.node.showBoundingBox(False)
            # ent = self.engine.entityMgr.getNextEnt()
            # self.engine.entityMgr.selectedEntities = []            
            # ent.node.showBoundingBox(True)


    def addNextEnt(self):
        ent = self.engine.entityMgr.getNextEnt()
        ent.node.showBoundingBox(True)
        self.engine.entityMgr.selectedEntities.append(ent)

    def selectNextEnt(self):
        for ent in self.engine.entityMgr.selectedEntities:
            ent.node.showBoundingBox(False)
        self.engine.entityMgr.selectedEntities = []
        self.addNextEnt()


    def stop(self):
        pass
    
    def checkPointAt(self, x, y):
        if (self.teamCheck(x, y)):
            self.engine.gameMgr.teamCheck = True
            print True

        elif (self.instructionCheck(x, y)):
            self.engine.gameMgr.instructionsCheck = True
            #change overlay
            print True

        elif (self.creditCheck(x, y)):
            self.engine.gameMgr.creditsCheck = True
            #change overlay
            print True
        
        elif (self.backCheck(x, y)):
            self.engine.gameMgr.backCheck = True
    
        
        elif (self.p1LCheck(x, y)):
            cursor = self.engine.gameMgr.p1Team
            cursor -= 1

            if (cursor < 0):
   
            #change to number of teams
                cursor = 1

            self.engine.gameMgr.p1Team = cursor  
            #scroll between available teams
            print "1Left"
        elif (self.p2RCheck(x, y)):
            cursor = self.engine.gameMgr.p2Team
            cursor += 1

            #change to number of teams
            if (cursor > 1):
                cursor = 0

            self.engine.gameMgr.p1Team = cursor  
            
            print "2Right"
        
        elif (self.p1LCheck(x, y)):
            cursor = self.engine.gameMgr.p2Team
            cursor -= 1

            if (cursor < 0):
   
            #change to number of teams
                cursor = 1

            self.engine.gameMgr.p1Team = cursor  
            #scroll between available teams
            print "1Left"
        elif (self.p2RCheck(x, y)):
            cursor = self.engine.gameMgr.p2Team
            cursor += 1

            #change to number of teams
            if (cursor > 1):
                cursor = 0

            self.engine.gameMgr.p2Team = cursor  
            
            print "2Right"
   
        elif (self.startCheck(x,y)):
            self.engine.gameMgr.startCheck = True

    def backCheck(self, x, y):
        return x > 0 and x < 100  and y >  self.windowHeight - 100 and y < self.windowHeight 

    def startCheck(self, x, y):
        return x > self.buttonStartX and x < self.buttonStartX+300  and \
               y > self.buttonStartY and y < self.buttonStartY+40 

    def instructionCheck(self, x, y):
        return x > self.buttonStartX and x < self.buttonStartX+300  and \
               y > self.buttonInstructY and y < self.buttonInstructY+40 

    def creditCheck(self, x, y):
        return x > self.buttonStartX and x < self.buttonStartX+300  and \
               y > self.buttonCreditsY and y < self.buttonCreditsY+40 

    def teamCheck(self, x, y):
        return x > self.buttonStartX and x < self.buttonStartX+300  and \
               y > self.buttonTeamSelectionY and y < self.buttonTeamSelectionY+40 
   
# Tweak this so that we have team selection working

    def p1LCheck(self, x, y):
        print "p1LCheck"
        return x > 0 and x < 300  and y > 0 and y < 300

    def p1RCheck(self, x, y):
        print "p2RCheck"
        return x > 350 and x < 600  and y > 0 and y < 300
  
    def p2LCheck(self, x, y):
        print "p2LCheck"
        return x > 100 and x < 250  and y > 530 and y < 560

    def p2RCheck(self, x, y):
        print "p2RCheck"
        return x > 100 and x < 250  and y > 530 and y < 560


