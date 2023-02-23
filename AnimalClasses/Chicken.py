from HW7.AbstractClasses.NotFlyingBirds import NotFlyingBirds


class Hen(NotFlyingBirds):
    def __init__(self, name, height, weight, colorEye):
        super().__init__(name, height, weight, colorEye)
    
    def makeNoise(self):
        print(f"{super().makeNoise()} 'Ко-ко-ко'")
    
    def __str__(self) -> str:
        return super().__str__()