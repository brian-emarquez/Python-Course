import pickle

fichero= open("Lista_nombres","rb") # leemos el archivo binario

lista = pickle.load(fichero) #Metodo Leoad para Leer y lo asgnamos a lista
print(lista)