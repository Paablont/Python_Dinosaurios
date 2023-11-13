from Dinosaurio import Dinosaurio


class Triceratops(Dinosaurio):
    def __init__(self, vida, energia,posicion):
        super().__init__(vida, energia,posicion)

    def desplazar(self,cantidad):
        super().desplazar()
        self.energia -= 5

