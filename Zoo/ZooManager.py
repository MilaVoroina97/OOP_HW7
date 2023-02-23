import copy
import Creator
import Zoo.Zoo
import AbstractClasses
import Interfaces

def showAll():
    for i in range(len(Zoo.Zoo.allZoo)):
        print(f"{i+1}) {Zoo.Zoo.allZoo[i]}")


def showInfo(num):
    print(f"{num-1}) {Zoo.Zoo.allZoo[num-1]}")
    if (isinstance(Zoo.Zoo.allZoo[num-1], AbstractClasses.Pet)):
        Zoo.Zoo.allZoo[num-1].showAffection()
    if (isinstance(Zoo.Zoo.allZoo[num-1], Interfaces.Train)):
        Zoo.Zoo.allZoo[num-1].canTrain()
    if (isinstance(Zoo.Zoo.allZoo[num-1], AbstractClasses.FlyingBirds)):
        Zoo.Zoo.allZoo[num-1].fly()


def makeAllNoise():
    for i in range(len(Zoo.allZoo)):
        Zoo.Zoo.allZoo[i].makeNoise()


def makeAnimalNoise(num):
    Zoo.Zoo.allZoo[num-1].makeNoise()


def addAnimal(num):
    match num:
        case 1:
            animal = Creator.createCat()
            Zoo.Zoo.allZoo.append(copy.copy(animal))
        case 2:
           animal= Creator.createTiger()
           Zoo.Zoo.allZoo.append(copy.copy(animal))
        case 3:
            animal = Creator.createDog()
            Zoo.Zoo.allZoo.append(copy.copy(animal))
        case 4:
            animal = Creator.createWolf()
            Zoo.Zoo.allZoo.append(copy.copy(animal))
        case 5:
           animal = Creator.createChicken()
           Zoo.Zoo.allZoo.append(copy.copy(animal))
        case 6:
            animal = Creator.createStork()
            Zoo.Zoo.allZoo.append(copy.copy(animal))

def deleteAnimal(num):
    Zoo.Zoo.allZoo.pop(num-1)