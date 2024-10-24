class Juego():

    def __init__(self):
        self.turn = 0 # si turno es par le toca al jugador, caso contrario a la compu 

    def combate(self, participante1, participante2):
        if participante1.velocidad < participante2.velocidad: self.turn = 1

        while True:
            if self.turn % 2 == 0:
                eleccion = self.eleccion()
                match eleccion():
                    case 1 : participante1.atacar()
                    case 2 : participante1.defender()
                    case 3 : participante1.perder_vida()
                    case 4 : participante1.curar()
                break
                
    def menu():
        print("Menu de opciones:"),
        print("1- ATACAR n\
               2- DEFENDER n\
               3- ENVENENAR n\
               4- CURAR n\
               ")

    def eleccion():
        menu()
        eleccion = int(input("Elige tu próximo movimiento:"))
        while eleccion > 4 or < 1 :
            print("Elige una opción válida")
            menu()
            eleccion = int(input("Elige tu próximo movimiento:"))
        return  eleccion


        