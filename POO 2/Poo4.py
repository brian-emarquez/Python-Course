#poo4 
#Contructores
#Encapsulamiento

class Coche(): #clase

    def __init__(self): # Contructor, podremos tenern un punto de partida    
        
        #Encapculacion __
        self.__largoChasis = 200 #Self
        self.__anchoClasis = 120
        self.__ruedas = 4 
        self.__enmarcha = True


    def arrancar(self,arrancamos): #metodo

        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "El coche esta en marcha"     
        else:
            return "El coche esta parado"

    def estado(self):
        print("El auto tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoClasis, "y un largo de ", self.__largoChasis)       

###################################################################

#Objeto
micoche=Coche() #Instanciar un clase
print(micoche.arrancar(True))
micoche.estado()

print("----------SEGUNDO OBJETO-----------\n")

micoche2=Coche() #Instanciar un clase
print(micoche2.arrancar(False))
micoche2.__ruedas=2 #Vemo sque no se cambiar el numero de ruedas, por que esta encapsulada
micoche2.estado()




