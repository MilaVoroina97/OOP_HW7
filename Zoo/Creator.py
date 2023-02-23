from HW7.AbstractClasses.AbstractParams import AbstractParams
from HW7.AnimalClasses.Cat import Cat
import AnimalClasses
import AbstractClasses
from HW7.AnimalClasses.Chicken import Chicken
from HW7.AnimalClasses.Dog import Dog
from HW7.AnimalClasses.Stork import Stork
from HW7.AnimalClasses.Tiger import Tiger
from HW7.AnimalClasses.Wolf import Wolf


class Creator:
    def createCat()-> Cat:
        name = AbstractParams.getName()
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        breed = AbstractParams.getBreed()
        vactination = AbstractParams.getVactination()
        woolColor = AbstractParams.getWoolColor()
        birthDate = AbstractParams.getBirthDate()
        woolPresence = AbstractParams.getWoolPresence()
        cat = AnimalClasses.Cat(height, weight, colorEye, name, breed, vactination, woolColor, birthDate, woolPresence)
        return cat

    def createDog() -> Dog:
        name = AbstractParams.getName()
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        breed = AbstractParams.getBreed()
        vactination = AbstractParams.getVactination()
        woolColor = AbstractParams.getWoolColor()
        birthDate = AbstractParams.getBirthDate()
        train = AbstractParams.getTrain()
        dog = AnimalClasses.Dog(height, weight, colorEye, name, breed, vactination, woolColor, birthDate,train)
        return dog
    
    def createChicken() -> Chicken:
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        chicken = AnimalClasses.Chicken(height, weight, colorEye)
        return chicken
    
    def createStork() -> Stork:
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        flyHeight = AbstractParams.getFlyHeight()
        stork = AnimalClasses.Stork(height, weight, colorEye,flyHeight)
        return stork
    
    def createTiger() -> Tiger:
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        birthDate = AbstractParams.getBirthDate()
        habitat = AbstractParams.getHabitat()
        tiger = AnimalClasses.Tiger(height, weight, colorEye, habitat, birthDate)
        return tiger
    
    def createWolf() -> Wolf:
        height = AbstractParams.getHeight()
        weight = AbstractParams.getWeight()
        colorEye = AbstractParams.getEyeColor()
        birthDate = AbstractParams.getBirthDate()
        habitat = AbstractParams.getHabitat()
        leader = AbstractParams.getLeader()
        wolf = AnimalClasses.Wolf(height, weight, colorEye, habitat, birthDate, leader)
        return wolf
        
        
                

        

        
       