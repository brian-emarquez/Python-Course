# Recuperar Objetos

import pickle
from SerializacionII import *

ficheroApertura = open("LosCoches","rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:
    print(i.estado())
