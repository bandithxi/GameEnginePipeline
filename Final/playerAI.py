class PlayerAI:
    def __init__(self, ent):
        self.ent = ent
        self.actionList = []
        
    def tick(self, dtime):
        if len(self.actionList) > 0:
            self.actionList[0].tick(dtime)
