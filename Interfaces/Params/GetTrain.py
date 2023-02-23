class GetTrain:
    def getTrain()->bool:
        train = input("Enter if this animal can be trained : yes or not")
        res = False
        if(train == "yes"):
            res = True
        else:
            res = False
        return res
