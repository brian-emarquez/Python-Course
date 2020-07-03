# Serializacion
# Guardar en fichero externo codificado en codigo binario "01010101010101010"
# Se usa la biblioteca Pickle - se usa lo metodos: dump() y load()

import pickle

lista_Nombre= ["Brian", "Ana", "Maria", "Isabel"]

fichero_binario=open("Lista_nombres","wb") # wb escrtura binaria

#volcado de la lista
pickle.dump(lista_Nombre, fichero_binario)

fichero_binario.close()

#Borrado de memoria (Opcional)
del (fichero_binario)