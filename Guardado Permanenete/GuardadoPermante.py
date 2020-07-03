import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self): # combierte en texto la cadena de texto la informacion del objeto
        return"{}{}{}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

    personas = []

    def __init__ (self):

        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        
        except:
            print("El fichero esto vacio")
            
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostarPersonas(self):
        print("La Informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

# Objetos
miLista = ListaPersonas()
persona = Persona("sandras ","Femeninos ", 30)
miLista.agregarPersonas(persona)
miLista.mostarPersonas()