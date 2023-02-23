from HW7.AbstractClasses.FlyingBirds import FlyingBirds


class Stork(FlyingBirds):
    def __init__(self, name, height, weight, colorEye,flyHeight):
        super().__init__(name, height, weight, colorEye, flyHeight)
    
    def makeNoise(self):
        print(f"{super().makeNoise()} 'Так-так-так-так' ")
    
    def birdFly(self):
        FlyingBirds.fly(self)
    
    def __str__(self) -> str:
        return super().__str__()