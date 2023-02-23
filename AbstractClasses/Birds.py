from HW7.AbstractClasses.Animal import Animal


class Birds(Animal):
    def __init__(self,height, weight, colorEye):
        super(Birds,self).__init__(height, weight, colorEye)