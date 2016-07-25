import random

class Monster:
    name = ''
    strength = 0
    willpower = 0
    description = ''

    def defense(self, attackNumber):
        defenseNumber = self.strength + random.randint(1, 6)
        print(self.name + ' se brani s utocnym cislem ' + str(defenseNumber))
        if defenseNumber > attackNumber:
            return 1
        elif defenseNumber < attackNumber:
            return 2
        else:
            return 3

    def showInfo(self):
        print('Prisera: ' + self.name)
        print('Sila: ' + str(self.strength))
        print('Vule: ' + str(self.willpower))
        print('Popis: ' + self.description)

class Skeleton(Monster):

    def __init__(self):
        self.name = "Kostlivec"
        self.strength = 4
        self.willpower = 2
        self.description = 'Obavany a prohnily kostlivec'
