import personaje
import random

class Vibora(personaje.Personaje):

    def __init__(self, name, vida, fuerza, resistencia, velocidad, toxicidad):
        super().__init__(name, vida, fuerza, resistencia, velocidad)
        self.toxicicdad = toxicidad

    def atacar(self):
        return self.fuerza * random.randint(0,5)
    
    def envenenar(self, objetivo):
        objetivo.estado["envenenado"] = self.toxicicdad * random.randint(0,5)
