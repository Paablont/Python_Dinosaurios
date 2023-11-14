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

while rondas > 0:
    if len(listaDinos)-1 == 0:
        print("Todos los dinos han muerto. Fin de la simulacion")
        rondas = 0
    else:
        print(f"******************** Ronda numero {rondas} ***********************")
        for a in listaDinos:
            print("------------------------------------------------------")
            print(f"TURNO DE:")
            print(f"{a}")

            accion = random.randint(1, 3)
            if accion == 1:
                posAntigua = a.posicion
                casillas = random.randint(1, 10)
                a.desplazar(casillas)
                if a.energia == 0:
                    print(f"{a.nombre} se ha quedado sin energia por tanto ha muerto")
                    listaDinos.remove(a)
                else:
                    print(
                        f"{a.nombre} se ha movido {casillas} casillas. Su posicion actual es {a.posicion} (antes {posAntigua})")
            if accion == 2:
                energiaAntigua = a.energia
                a.comer()
                print(f"{a.nombre} ha comido. Su energia ha pasado de {energiaAntigua} a {a.energia}")
                print()
            if accion == 3:
                numPresa = random.randint(1, len(listaDinos) -1 )

                presa = listaDinos[numPresa]
                if isinstance(a, Trike):
                    print("Los trikes no atacan")
                else:
                    print(f"{a.nombre} va a atacar a {presa.nombre}:")
                    quienVive = a.atacar(presa)
                    # Si quienVive es 0 muere la presa, si es 1 muere el atacante
                    if quienVive == 0:
                        presa.vida = 0
                        print(f"La presa {presa.nombre} ha muerto")
                        listaDinos.remove(presa)
                    else:
                        a.vida = 0
                        print(f"El atacante {a.nombre} ha muerto")
                        listaDinos.remove(a)
            print("------------------------------------------------------")

            print()
        print("************************************************************")
        seguir = input("Deseas seguir con la simulacion? S si, N no").upper()
    if seguir == "S":
        rondas -= 1
    else:
        rondas = 0
        print("Se ha acabado la simulacion")
