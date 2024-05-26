# Serializacion de Objetos
import pickle


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
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


Coche1=Vehiculos("Mazda","Mx5")
Coche2=Vehiculos("seat","Leon")
Coche3=Vehiculos("Renault","Megane")

coches =[Coche1, Coche2, Coche3]
fichero = open("LosCoches","wb")

pickle.dump(coches, fichero)
fichero.close()

del(fichero)

