import AIaction as action
class AIMgr:
	#AI Mgr will manager FSM of team 
	#AI aspect will manage FSM of players
    def __init__(self, engine):
        self.engine = engine
        self.ball = self.engine.entityMgr.ball
        self.team1 = self.engine.entityMgr.team1
        self.team2 = self.engine.entityMgr.team2
        self.half = self.engine.gameMgr.half
        self.whoHasBall = 0
        self.entityMgr = self.engine.entityMgr
        #self.simpleAI = True

    def init(self):

    	pass

    def tick(self, dt):
        ball = self.engine.entityMgr.ball
        
        if (ball.attachEnt):
            self.whoHasBall = ball.attachEnt.team

        if (self.whoHasBall == 1):
        	for ent in self.entityMgr.team2.values():
        		ent.aspects[2].clear()

        		if (ent != self.engine.entityMgr.selectedEntP2):
        		    self.entityMgr.addAction(ent, action.Intercept(ent, ball.attachEnt))
                pass
        elif (self.whoHasBall == 2):
            for ent in self.entityMgr.team1.values():
                ent.aspects[2].clear()

                if (ent != self.engine.entityMgr.selectedEntP1):
                    self.entityMgr.addAction(ent, action.Intercept(ent, ball.attachEnt))
                pass
        pass