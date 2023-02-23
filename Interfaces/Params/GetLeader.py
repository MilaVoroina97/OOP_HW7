class GetLeader:
    def getLeader()->bool:
        leader = input("Enter if this animal a leader : yes or not")
        res = False
        if(leader == "yes"):
            res = True
        else:
            res = False
        return res