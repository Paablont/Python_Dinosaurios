from Dinosaurio import *

class Trike(Dinosaurio):
    def __init__(self,nombre, vida, energia,posicion):
        super().__init__(nombre,vida, energia,posicion)

    def desplazar(self,casillas):
        super().desplazar(casillas)
        for a in range(casillas):
            self.energia -= 5






