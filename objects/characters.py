import random
import logging

class Character:
    'Common base class for all characters'
    name = ''
    strength = 0

    def getStrength(self):
        return self.strength

    def getName(self):
        return self.name

    def attack(self, Monster):
        attackNumber = self.getStrength() + random.randint(1, 6)
        print(self.getName() + ' utoci na priseru ' + Monster.getName())
        defenseResult = Monster.defense(attackNumber)

        if defenseResult == 1:
            print("Bohuzel te prisera porazila!")
        elif defenseResult == 2:
            print("Vyhral si!")
        else:
            print("Doslo k remize!");


class Warrior(Character):
    'Warrior class'

    def __init__(self):
        self.name = 'Player1'
        self.strength = 5
