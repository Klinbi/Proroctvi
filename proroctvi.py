from objects.characters import *
from objects.monsters import *
from objects.structures import *
from objects.utils import *
from objects.items import *

# Start game

print('Vitejte ve hre Proroctvi')
print()
print('Co si prijete?')
print('1 - Bojovat')
print('2 - Zobrazit inventar')

choice = int(input("Zvolte moznost: "))
print()

if choice == 1:
    # Select character
    player1 = Ranger()

    print('Zvolili jste si postavu:')
    print()
    player1.showInfo()
    print()

    # Monster fight
    monster1 = Skeleton()
    print('Zautocila na vas potvora:')
    monster1.showInfo()

    print()
    print('Boj zacina!')
    player1.attack(monster1)

elif choice == 2:
    connector = DBConnector('proroctvi.db')
    hammer = HammerOfJustice()
    connector.insertItem(hammer)
    hammerFromDb = connector.getItem(hammer.name)
    print('V inventari mate:')
    print()
    hammerFromDb.showInfo()
