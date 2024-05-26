#poo 2

class Coche(): #clase
    largoChasis = 200 #propiedades
    anchoCalsis = 120
    ruedas = 4
    enmarcha = False


    def arrancar(self): #metodo
        self.enmarcha = True


    def estado(self): #metodo
        if(self.enmarcha):
            return "El coche esta en marcha"     
        else:
            return "El coche esta parado"
        #pass #para queno de error

#########################################################################

#Objeto
micoche=Coche() #Instanciar un clase

print("El largo del coche es: ",micoche.largoChasis) #Nomenchatura del punto
print("El Coche tiene: ", micoche.ruedas, "ruedas")
micoche.arrancar()

print(micoche.estado())
print("----------------A continiacion creamos el segundo objetos-----------------")

micoche2 = Coche()
print("El largo del coche es: ",micoche2.largoChasis) #Nomenchatura del punto
print("El Coche tiene: ", micoche2.ruedas, "ruedas")
print(micoche2.estado())



