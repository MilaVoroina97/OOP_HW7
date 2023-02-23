import copy
import Creator
import Zoo
import AbstractClasses
import Interfaces

def showAll():
    for i in range(len(Zoo.allZoo)):
        print(f"{i+1}) {Zoo.allZoo[i]}")


def showInfo(num):
    print(f"{num-1}) {Zoo.allZoo[num-1]}")
    if (isinstance(Zoo.allZoo[num-1], AbstractClasses.Pet)):
        Zoo.all[num-1].showAffection()
    if (isinstance(Zoo.allZo[num-1], Interfaces.Train)):
        Zoo.all[num-1].canTrain()
    if (isinstance(Zoo.allZo[num-1], AbstractClasses.FlyingBirds)):
        Zoo.allZoo[num-1].fly()


def makeAllNoise():
    for i in range(len(Zoo.allZoo)):
        Zoo.allZoo[i].makeNoise()


def sayAnimal(num):
    Zoo.allZoo[num-1].makeNoise()


def addAnimal(num):
    match num:
        case 1:
            animal = Creator.createCat()
            Zoo.allZoo

        case 2:
            Creator.createTiget()
        case 3:
            Creator.createDog()
        case 4:
            Creator.createWolf()
        case 5:
            Creator.createChicken()
        case 6:
            Creator.createStork()

def deleteAnimal(num):
    Zoo.allZoo.pop(num-1)