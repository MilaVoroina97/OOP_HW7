class GetWoolPresence:
    def getWoolPresence()->bool:
        woolPresense = input("Enter if this animal can be trained : yes or not")
        res = False
        if(woolPresense == "yes"):
            res = True
        else:
            res = False
        return res