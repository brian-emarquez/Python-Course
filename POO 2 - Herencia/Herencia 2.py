#Herencia 2 
#Sobre escritura de metodos
#Herencia simple y muliple

#que comportamientos en comun tienen todos los objetos?
#Sobre escritura de metodos

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
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)



#Herencia
class Moto(Vehiculos):
    hcaballito = None
    #hcaballito = ""

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    #Remplaza al "Estado de la Super clase
    #Sobre escritura de metodos
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n",self.hcaballito)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

miMoto = Moto("Holda","CBR")
miMoto.caballito()
miMoto.estado()



