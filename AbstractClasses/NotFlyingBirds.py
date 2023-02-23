from HW7.AbstractClasses.Birds import Birds


class NotFlyingBirds(Birds):
    def __init__(self,height, weight, colorEye):
        super(NotFlyingBirds,self).__init__(height, weight, colorEye)