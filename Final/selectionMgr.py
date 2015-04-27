import ogre.io.OIS as OIS
    
class SelectionMgr:

    def __init__(self, engine):
        self.engine = engine

    def init(self):
        self.keyboard = self.engine.inputMgr.keyboard
        self.toggle = 0.1

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
        if (self.startCheck(x, y)):
            self.engine.gameMgr.startCheck = True
            self.engine.guiMgr.overlay.hide()
            self.engine.guiMgr.hud2.show()
            
            print True

        elif (self.instructionCheck(x, y)):
            self.engine.gameMgr.instruction = True
            #change overlay
            print True

        elif (self.creditCheck(x, y)):
            self.engine.gameMgr.credit = True
            #change overlay
            print True

    def startCheck(self, x, y):
        return x > 100 and x < 250  and y > 400 and y < 450

    def instructionCheck(self, x, y):
        return x > 100 and x < 250  and y > 455 and y < 480

    def creditCheck(self, x, y):
        return x > 100 and x < 250  and y > 490 and y < 520

