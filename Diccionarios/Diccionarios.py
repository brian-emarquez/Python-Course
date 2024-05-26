#Diccionarios

print("==============================================================================================")
#volverlo Inmutable
print("Tipo Diccionario")
diccionario = {}
print(type(diccionario))

print("==============================================================================================")

diccionario = {"Azul": "Blue", "Rojo":"Red", "Amarillo":"Yellow"}
print(diccionario)
print()
print("\t.:¿Como es azul en Ingles?:.")
print(diccionario["Azul"])
print()

print("Agregar al diccionario")
#agregamos
diccionario["negro"]= "black"
print(diccionario)

print("Borrar al Diccionario")
#borrar
del (diccionario["Azul"])
print(diccionario)


print("==============================================================================================")

productos = {
    "nombre": "libro",
    "cantidad": 3,
    "precio": 4.00
}


persona = {
    "nombres": "brian",
    "apellidos" : "Marquez"
}

print (productos)
print (persona)

#utilizando los metodos de Dir()
print(productos.keys()) # ,uestras lso nombres de la claves

#Eliminar en un diccionario
#del productos

#eliminar elementos
persona.clear()
print(persona)