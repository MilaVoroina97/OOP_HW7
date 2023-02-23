from HW7.AbstractClasses.Animal import Animal


class Wild(Animal):
    def __init__(self,height, weight, colorEye, habitat, birthDate):
        self.habitat = habitat
        self.birthDate = birthDate
        super(Wild, self).__init__(height, weight, colorEye)