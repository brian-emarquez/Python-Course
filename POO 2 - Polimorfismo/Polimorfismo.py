#POO 2 - POLIFORMISMO
#

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me Desplazo utilizando dos Ruedas")

class Camion():

    def desplazamiento(self):
        print("Me Desplazo utilizando seis Ruedas")


#Polimorfismo
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Camion()
desplazamientovehiculo(mivehiculo)



