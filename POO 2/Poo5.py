#poo5
#Encapsulacion de metodos

class Coche(): #clase

    def __init__(self): # Contructor, podremos tenern un punto de partida    
        
        #Encapculacion __
        self.__largoChasis = 250 #Self
        self.__anchoClasis = 120
        self.__ruedas = 4 
        self.__enmarcha = False


    def arrancar(self,arrancamos): #metodo
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El Coche esta en marcha"  

        elif(self.__enmarcha and chequeo==False):
            return "Algo ah do al el el chequeo . no se puede arrancar"  

        else:
            return "El coche esta parado"


    def estado(self):
        print("El auto tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoClasis, "y un largo de ", self.__largoChasis)       


    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


#############################################################################

#Objeto
micoche=Coche() #Instanciar un clase
print(micoche.arrancar(True))
micoche.estado()

print("----------SEGUNDO OBJETO-----------\n")

micoche2=Coche() #Instanciar un clase
print(micoche2.arrancar(False))
micoche2.estado()




