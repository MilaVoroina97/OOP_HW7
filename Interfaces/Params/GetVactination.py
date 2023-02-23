class GetVactination:
    def getVactination()->bool:
        vactinated = input("Enter if this animal can be trained : yes or not")
        res = False
        if(vactinated == "yes"):
            res = True
        else:
            res = False
        return res
