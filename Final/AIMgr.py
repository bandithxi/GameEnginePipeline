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
        self.whoHasBall = 1
        self.entityMgr = self.engine.entityMgr

    def init(self):

    	pass

    def tick(self, dt):
        if (self.whoHasBall == 1):
        	for ent in self.entityMgr.team2.values():
        		#ent.aspects[2].clear()
        		pass
        		#self.entityMgr.addAction(ent, action.Follow(ent, self.engine.entityMgr.ball))


        pass