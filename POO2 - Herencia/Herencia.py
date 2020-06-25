#Herencia
#Principal funcion en la POO es la Reuilizacion de Codigo

#¿QUE CARACTERISTICAS EN COMUN TIENE TODOS LO OBJETOS?
#que comportamientos en comun tienen todos los objetos?

#superclase
class Vehiculos():

    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo= modelo
        self.enmarcha=False
        self.acelera = False
        self.frena= False


    #definimos los comportamientos, metodos.

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn maehca: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)




#Herencia
class Moto(Vehiculos):
    pass

miMoto = Moto("Holda","CBR")
miMoto.estado()



