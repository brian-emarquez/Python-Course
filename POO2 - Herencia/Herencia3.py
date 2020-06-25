#Herencia 3

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

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n",self.hcaballito)


class VElectricos():
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


#Herencia
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La Furgoneta esta cargada"
        else:
            return "La furgoneta esta vacia"

#Herencia Multiple
class BicicletaElectrica(VElectricos, Vehiculos):
    pass




    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("------Obejeto 1-------\n")
miMoto = Moto("Holda","CBR")
miMoto.caballito()
miMoto.estado()

print("\n-------Objeto 2-------\n")
miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))





