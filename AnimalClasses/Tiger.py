from HW7.AbstractClasses.Wild import Wild


class Tiger(Wild):
   def __init__(self,height, weight, colorEye, habitat, birthDate):
      super(Tiger, self).__init__(height, weight, colorEye, habitat, birthDate)
   
   def makeNoise(self):
        print(f"{super().makeNoise()}  РРРррр")

   def __str__(self) -> str:
        return f"{super().__str__()}; Среда обитания: {self.habitat}; Дата нахождения: {self.birthDate};"