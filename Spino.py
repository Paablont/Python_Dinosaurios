from Dinosaurio import Dinosaurio


class Spino(Dinosaurio):
    def __init__(self, vida, energia,posicion):
        super().__init__(vida, energia,posicion)

    def desplazar(self,cantidad):
        super().desplazar()
        self.energia -= 2