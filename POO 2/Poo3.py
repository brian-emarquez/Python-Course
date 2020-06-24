#Poo3
#Envio de un valor

class Coche(): #clase
    largoChasis = 200 #propiedades
    anchoClasis = 120
    ruedas = 4
    enmarcha = True


    def arrancar(self,arrancamos): #metodo

        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"     
        else:
            return "El coche esta parado"

    def estado(self):
        print("El auto tiene ", self.ruedas, " ruedas. un ancho de ", self.anchoClasis, "y un largo de ", self.largoChasis)       


#Objeto
micoche=Coche() #Instanciar un clase


print(micoche.arrancar(True))
micoche.estado()

print("----------SEGUNDO OBJETO-----------\n")
micoche2=Coche() #Instanciar un clase


print(micoche2.arrancar(False))
micoche2.estado()




