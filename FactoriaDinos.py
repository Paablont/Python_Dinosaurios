import random

from Trike import *
from Rex import *
from Spino import *


# Factoría
listaDinos = []
vida = 100
energia = 100

def crearDinos():
    # Creamos 3 trikes, 3 rexes y 3 spinos
    for a in range(3):
        trike = Trike("Trike " + str(a), vida, energia, posicion=random.randint(1, 100))
        rex = Rex("Rex " + str(a), vida, energia, posicion=random.randint(1, 100))
        spino = Spino("Spino " + str(a), vida, energia, posicion=random.randint(1, 100))

        listaDinos.append(trike)
        listaDinos.append(rex)
        listaDinos.append(spino)
    return listaDinos


