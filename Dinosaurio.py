class Dinosaurio:
    def __init__(self,nombre, vida, energia,posicion):
        self.nombre = nombre
        self.vida = vida
        self.energia = energia
        self.posicion = posicion
        # self.probSobrevivir = probSobrevivir

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        self._vida = vida


    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, energia):
        self._energia = energia

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion
    @property
    def probSobrevivir(self):
        return self._probSobrevivir

    @probSobrevivir.setter
    def probSobrevivir(self,probSobrevivir):
         self._probSobrevivir = probSobrevivir

    def comer(self):
        self.energia = 100

    def desplazar(self,casillas):
        self.posicion += casillas

    def __str__(self):
        return (f"Nombre: {self.nombre} \n"
                f"Vida: {self.vida}\n"
                f"Energia: {self.energia}\n"
                f"Posicion: {self.posicion}\n")







