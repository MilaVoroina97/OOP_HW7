from abc import ABC, abstractmethod

from HW7.AbstractClasses.Animal import Animal
from HW7.Interfaces.ShowAffection import ShowAffection

class Pet(Animal,ShowAffection):
    def __init__(self, height, weight, colorEye, name, breed, vaccination, woolColor, birthDate):
        self.name = name
        self.breed = breed
        self.vaccination = vaccination
        self.woolColor = woolColor
        self.birthDate = birthDate
        super(Pet, self).__init__(height, weight, colorEye)
    @abstractmethod
    def showAffection(self):
         return super().showAffection()
    def __str__(self) -> str:
        return (f"{super().__str__()} Кличка: {self.name}; Порода: {self.breed}; " 
        f"Наличие прививки: {self.vaccination}; Цвет: {self.color}; Дата рождения: {self.birthDate};")
    

    

    