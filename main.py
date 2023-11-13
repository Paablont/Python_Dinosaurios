import random
import time
from Dinosaurio import  *
from Trike import *
from Rex import *
from Spino import *
from FactoriaDinos import *
listaDinos = []
listaDinos = crearDinos()
salir = True

rondas = 5
while rondas > 0:
    for a in listaDinos:
        print(f"Nombre: {a.nombre} , Posicion: {a.posicion}")
        casillas = random.randint(1,10)
        a.desplazar(casillas)
        print(f"Nombre: {a.nombre} , Posicion: {a.posicion}")
        time.sleep(3)


    rondas -= 1
