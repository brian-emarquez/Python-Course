# Recuperar Objetos

import pickle
from SerializacionII import Vehiculos

ficheroApertura = open("LosCoches","rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:
    print(i.estado())
