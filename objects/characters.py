import random
import logging
from .structures import *

class Character:
    'Common base class for all characters'
    name = ''
    strength = 0
    willpower = 0
    homebases = []
    description = ''

    def attack(self, Monster):
        attackNumber = self.strength + random.randint(1, 6)
        print(self.name + ' utoci na priseru ' + Monster.name + ' s utocnym cislem ' + str(attackNumber))
        defenseResult = Monster.defense(attackNumber)

        if defenseResult == 1:
            print("Bohuzel te prisera porazila!")
        elif defenseResult == 2:
            print("Vyhral si!")
        else:
            print("Doslo k remize!");

    def showInfo(self):
        print('Postava: ' + self.name)
        print('Sila: ' + str(self.strength))
        print('Vule: ' + str(self.willpower))
        print('Domovske mista: ')
        for homebase in self.homebases:
            print('* ' + homebase.name)
        print('Popis: ' + self.description)

class Ranger(Character):
    'Ranger class'

    def __init__(self):
        self.name = 'Hranicarka'
        self.strength = 5
        self.willpower = 2
        self.homebases = [ForestCamp(), Fortress()]
        self.description = 'Tohle je nemilosrdna hranicarka'
