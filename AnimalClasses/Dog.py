from HW7.AbstractClasses.Pet import Pet
from HW7.Interfaces.Train import Train


class Dog(Pet,Train):
    def __init__(self,height, weight, colorEye, name, breed, vaccination, woolColor, birthDate,train):
        self.train = train
        super(Dog, self).__init__(height, weight, colorEye, name, breed, vaccination, woolColor, birthDate)
    
    def makeNoise(self):
        print(f"{super().makeNoise()} 'Гав-гав'")
    
    def showAffection(self):
        return (super().showAffection())
    
    def canTrain(self):
        Train.canTrain(self)

    def __str__(self) -> str:
        return (f"{super().__str__()} Поддается ли дрессировке: {self.train};")
    