import random

class Personaje:

    def __init__(self, name, vida, fuerza, resistencia, velocidad):
        self.name = name
        self.vida = vida
        self.fuerza = fuerza
        self.resistencia = resistencia
        self.velocidad = velocidad
        self.estado = {"envenenado": 0, "paralizado":0, "dormido": 0, "quemado":0 }

    def atacar(self):
        return self.fuerza * random.randint(0,5)
    

    def defender(self):
        pass

    def perder_vida(self, damage):
        self.vida = self.vida - damage

    def curar(self, curacion):
        self.vida = self.vida + curacion
