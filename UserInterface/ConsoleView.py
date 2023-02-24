import View
import Zoo.ZooManager
import Zoo.Zoo

def start():
    num = View.menu()
    match num:
        case 1:
            addAnimal()
        case 2:
            deleteAnimal()
        case 3:
            showAnimalInfo()
        case 4:
            makeAnimalNoise()    
        case 5:
            Zoo.ZooManager.showAll()
            start()
        case 6:
            Zoo.ZooManager.makeAllNoise()
            start()
        case 7:
            exit()


def addAnimal():
    num = View.addAnimalMenu()
    if (num > len(Zoo.Zoo.allZoo)):
        start()
    else:
        Zoo.ZooManager.addAnimal(num)
        start()


def deleteAnimal():
    Zoo.ZooManager.showAll()
    num = View.delAnimalMenu()
    if (num > len(Zoo.Zoo.allZoo)):
        start()
    else:
        Zoo.ZooManager.deleteAnimal(num)
        start()


def makeAnimalNoise():
    Zoo.ZooManager.showAll()
    num = View.makeNoiseAnimalMenu()
    if (num > len(Zoo.Zoo.allZoo)):
        start()
    else:
        Zoo.ZooManager.makeAnimalNoise(num)
        start()


def showAnimalInfo():
    Zoo.ZooManager.showAll()
    num = View.showAnimalMenu()
    if (num > len(Zoo.Zoo.allZoo)):
        start()
    else:
        Zoo.ZooManager.showInfo(num)
        start()