from HW7.AbstractClasses.Wild import Wild
from HW7.Interfaces.Leader import Leader


class Wolf(Wild,Leader):
    def __init__(self, name, height, weight, colorEye, habitat, birthDate, leader):
      self.leader = leader
      super(Wolf, self).__init__(name, height, weight, colorEye, habitat, birthDate)
   
    def makeNoise(self):
        print(f"{super().makeNoise()} уууУУУ")

    def canBeLeader(self) -> str:
       Leader.canBeLeader(self)

    def __str__(self) -> str:
      if (self.leader == True):
        return f"{super().__str__()}; Среда обитания: {self.habitat}; Дата нахождения: {self.birthDate}; Вожак стаи"
      else: return f"{super().__str__()} Среда обитания: {self.habitat}; Дата нахождения: {self.birthDate};"