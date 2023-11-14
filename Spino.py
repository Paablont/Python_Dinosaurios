import random
from Dinosaurio import Dinosaurio
from Rex import *
from Trike import *


class Spino(Dinosaurio):
    def __init__(self, nombre, vida, energia, posicion):
        super().__init__(nombre, vida, energia, posicion)

    def desplazar(self,casillas):
        super().desplazar(casillas)
        for a in range(casillas):
            self.energia -= 2

    def atacado(self,probabilidad):
        if probabilidad <= 5:
            self.vida = 0

    def atacar(self,presa):
        if isinstance(presa,Trike):
            sobrevive = random.randint(1,10)
            if sobrevive >= 3:
                self.vida = 0
        if isinstance(presa,Spino) or isinstance(presa,Rex):
            sobrevive = random.randint(0, 1)
            if sobrevive == 1:
                self.vida = 0




