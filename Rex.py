from Dinosaurio import Dinosaurio


class Rex(Dinosaurio):
    def __init__(self, vida, energia,posicion):
        super().__init__(vida, energia,posicion)

    def desplazar(self,cantidad):
        super().desplazar()
        self.energia -= 1