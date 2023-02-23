from HW7.AbstractClasses.Pet import Pet



class Cat(Pet):
    def __init__(self,height, weight, colorEye, name, breed, vaccination, woolColor, birthDate, woolPresence):
        self.woolPresence = woolPresence
        super(Cat, self).__init__(height, weight, colorEye, name, breed, vaccination, woolColor, birthDate)
    
    def makeNoise(self):
        print(f"{super().makeNoise()} 'Мяу'")
    
    def showAffection(self):
        return (super().showAffection())

    def __str__(self) -> str:
        return (f"{super().__str__()} Наличие шерсти: {self.woolPresence};")