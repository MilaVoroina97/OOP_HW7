from HW7.AbstractClasses.NotFlyingBirds import NotFlyingBirds


class Chicken(NotFlyingBirds):
    def __init__(height, weight, colorEye):
        super().__init__(height, weight, colorEye)
    
    def makeNoise(self):
        print(f"{super().makeNoise()} 'Ко-ко-ко'")
    
    def __str__(self) -> str:
        return super().__str__()