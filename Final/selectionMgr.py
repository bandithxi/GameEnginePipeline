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
                self.selectNextEnt(2)
            else:
                self.selectNextEnt(1)

            # ent = self.engine.entityMgr.selectedEnt
            # ent.node.showBoundingBox(False)
            # ent = self.engine.entityMgr.getNextEnt()
            # self.engine.entityMgr.selectedEntities = []            
            # ent.node.showBoundingBox(True)


    def selectNextEnt(self, team):
        if (team == 1):
            for key, ent in self.engine.entityMgr.team1.iteritems():
                ent.node.showBoundingBox(False)
        else:
            for key, ent in self.engine.entityMgr.team2.iteritems():
                ent.node.showBoundingBox(False)
        ent = self.engine.entityMgr.getNextEnt(team)
        ent.node.showBoundingBox(True)
        
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
                cursor = 4

            self.engine.gameMgr.p1Team = cursor  
            #scroll between available teams
           
            #Show Flag
            self.showFlag(cursor)
            print "1Left"

        elif (self.p2LCheck(x, y)):
            cursor = self.engine.gameMgr.p2Team
            cursor -= 1

            #change to number of teams
            if (cursor < 0):
                cursor = 4

            self.engine.gameMgr.p1Team = cursor  

            #Show Flag
            self.showFlag(cursor)
            
            print "2Left"
        
        elif (self.p1RCheck(x, y)):
            cursor = self.engine.gameMgr.p1Team
            cursor += 1

            if (cursor > 4):
   
            #change to number of teams
                cursor = 0

            self.engine.gameMgr.p1Team = cursor  
            print "Cursor - " + str (cursor)
            #scroll between available teams

            #Show Flag
            self.showFlag(cursor)
            print "1Right"

        elif (self.p2RCheck(x, y)):
            cursor = self.engine.gameMgr.p2Team
            cursor += 1

            #change to number of teams
            if (cursor > 4):
                cursor = 0

            self.engine.gameMgr.p2Team = cursor  

            #Show Flag
            self.showFlag(cursor)
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
        #print "p1LCheck"
        return x > 170 and x < 310  and y > 250 and y < 375

    def p1RCheck(self, x, y):
        #print "p1RCheck"
        return x > 1295 and x < 1430  and y > 250 and y < 375
 
    def p2LCheck(self, x, y):
        #print "p2LCheck"
        return x > 170 and x < 310  and y > 755 and y < 880

    def p2RCheck(self, x, y):
        #print "p2RCheck"
        return x > 1295 and x < 1430  and y > 755 and y < 880

    def showFlag (self, cursor): 
        if cursor == 0:
                self.engine.guiMgr.flagRed.hide()
                self.engine.guiMgr.flagBlue.hide()
                self.engine.guiMgr.flagYellow.show()
        elif cursor == 1:
                self.engine.guiMgr.flagYellow.hide()                
                self.engine.guiMgr.flagRed.hide()
                self.engine.guiMgr.flagBlue.show()
        elif cursor == 2:
                self.engine.guiMgr.flagBlue.hide()
                self.engine.guiMgr.flagYellow.hide()                
                self.engine.guiMgr.flagRed.show()
        elif cursor == 3:
                self.engine.guiMgr.flagBlue.hide()
                self.engine.guiMgr.flagYellow.hide()                
                self.engine.guiMgr.flagRed.hide()
        elif cursor == 4:
                self.engine.guiMgr.flagBlue.hide()
                self.engine.guiMgr.flagYellow.hide()                
                self.engine.guiMgr.flagRed.hide()




