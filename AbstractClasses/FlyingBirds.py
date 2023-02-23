from HW7.AbstractClasses.Animal import Animal
from HW7.Interfaces.Fly import Fly
from abc import abstractmethod


class FlyingBirds(Animal,Fly):
    def __init__(self,height, weight, colorEye, flyHeight):
        self.flyHeight = flyHeight
        super(FlyingBirds,self).__init__(height, weight, colorEye)
    @abstractmethod
    def fly(self):
        return super().fly()