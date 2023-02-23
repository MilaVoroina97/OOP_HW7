class Leader:
    def canBeLeader(self)-> str:
        if (self.leader == True):
            return "This wolf is leader"
        else: 
            return "This wolf is not a leader"