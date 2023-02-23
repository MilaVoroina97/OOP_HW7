from abc import ABC, abstractmethod
from HW7.Interfaces.MakeNoise import MakeNoise

class Animal(ABC,MakeNoise):
    def __init__(self, height, weight, colorEye):
        self.height = height
        self.weight = weight
        self.colorEye = colorEye
    
    def __str__(self) -> str:
        return f"Рост: {self.height}; Вес: {self.weight}; Цвет глаз: {self.colorEye};"

    @abstractmethod
    def makeNoise(self):
        return super().makeNoise()

    

