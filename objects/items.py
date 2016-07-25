class Item:
    name = ''
    attackpower = ''
    description = ''

    def __init__(self, item):
        self.name = item[0]
        self.attackpower = item[1]
        self.description = item[2]

    def showInfo(self):
        print('Predmet: ' + self.name)
        print('Utocne cislo: ' + str(self.attackpower))
        print('Popis: ' + self.description)


class Sword(Item):

    def __init__(self):
        self.name = 'Mec krutosti'
        self.attackpower = 5
        self.description = 'Mec neskutecne krutosti'

class HammerOfJustice(Item):

    def __init__(self):
        self.name = 'Kladivo spravedlnosti'
        self.attackpower = 6
        self.description = 'Kladivo ktere vyresi jakkykoliv problem'
