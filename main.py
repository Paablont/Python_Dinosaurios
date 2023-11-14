import random
import time
from Dinosaurio import *
from Trike import *
from Rex import *
from Spino import *
from FactoriaDinos import *

listaDinos = []
listaDinos = crearDinos()
salir = True

rondas = 5
for a in listaDinos:

    print(f"******************** Ronda numero {rondas} ***********************")
    print(f"TURNO DE:")
    print(f" {a}")

    accion = random.randint(1, 3)
    if accion == 1:
        print("Desplazarse")
        casillas = random.randint(1, 10)
        a.desplazar(casillas)
        print(f"Nombre: {a.nombre} , Posicion: {a.posicion}")
    if accion == 2:
        print("Comer")
    if accion == 3:
        if isinstance(a,Trike):
            print("Los trikes no atacan")
        else:
            print("Atacar")



    print("************************************************************")
    print()
    rondas -= 1
    time.sleep(10)


