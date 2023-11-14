import random
from Dinosaurio import Dinosaurio
from Trike import *
from Spino import *

class Rex(Dinosaurio):
    def __init__(self, nombre, vida, energia, posicion):
        super().__init__(nombre, vida, energia, posicion)

    def desplazar(self,casillas):
        super().desplazar(casillas)
        for a in range(casillas):
            self.energia -= 1

    def atacado(self,probabilidad):
        if probabilidad <= 5:
            self.vida = 0

    def atacar(self,presa):
        #Esta variable sera 0 o 1 siendo 0 el atacante y 1 la presa
        vivo = 0
        if isinstance(presa,Trike):
            sobrevive = random.randint(1,10)
            if sobrevive >= 3:
                vivo = 0
            else:
                vivo = 1
        if isinstance(presa,Spino) or isinstance(presa,Rex):
            sobrevive = random.randint(0, 1)
            if sobrevive == 1:
                vivo = 0
            else:
                vivo = 1
        return vivo
