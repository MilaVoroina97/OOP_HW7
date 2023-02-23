from HW7.Interfaces.Params.GetBirthDate import GetBirthDate
from HW7.Interfaces.Params.GetBreed import GetBreed
from HW7.Interfaces.Params.GetEyeColor import GetEyeColor
from HW7.Interfaces.Params.GetFindDate import GetFindDate
from HW7.Interfaces.Params.GetFlyHeight import GetFlyHeight
from HW7.Interfaces.Params.GetHabitat import GetHabitat
from HW7.Interfaces.Params.GetHeight import GetHeight
from HW7.Interfaces.Params.GetLeader import GetLeader
from HW7.Interfaces.Params.GetTrain import GetTrain
from HW7.Interfaces.Params.GetVactination import GetVactination
from HW7.Interfaces.Params.GetWeight import GetWeight
from HW7.Interfaces.Params.GetWoolColor import GetWoolColor
from HW7.Interfaces.Params.GetWoolPresence import GetWoolPresence
from HW7.Interfaces.Params.GetName import GetName




class AbstractParams(GetBirthDate,GetBreed,GetEyeColor,GetFindDate,GetFlyHeight,GetHabitat,GetHeight,GetLeader,GetTrain,
GetVactination,GetWeight,GetWoolColor,GetWoolPresence,GetName):
    def getBirthDate() -> str:
        super().getBirthDate()
    def getBreed() -> str:
        super().getBreed()
    def getEyeColor() -> str:
        super().getEyeColor()
    def getFindDate() -> str:
        super().getFindDate()
    def getFlyHeight() -> int:
        super().getFlyHeight()
    def getHabitat() -> str:
        super().getHabitat()
    def getHeight() -> int:
        super().getHeight()
    def getLeader() -> bool:
        super().getLeader()
    def getTrain() -> bool:
        super().getTrain()
    def getVactination() -> bool:
        super().getVactination()
    def getWeight() -> int:
        super().getWeight()
    def getWoolColor() -> str:
        super().getWoolColor()
    def getWoolPresence() -> bool:
        super().getWoolPresence()
    def getName() -> str:
        return super().getName()




