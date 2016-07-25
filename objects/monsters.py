import random

class Monster:
    name = ''
    strength = 0
    
    def getStrength(self):
        return self.strength

    def getName(self):
        return self.name

    def defense(self, attackNumber):
        defenseNumber = self.getStrength() + random.randint(1, 6)
        if defenseNumber > attackNumber:
            return 1
        elif defenseNumber < attackNumber:
            return 2
        else:
            return 3

class Skeleton(Monster):

    def __init__(self):
        self.name = "Kostlivec"
        self.strength = 4
