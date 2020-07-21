# BBDDD II
# Insertar Varios Registros
# Reguperacion de registros

import sqlite3

miConexion = sqlite3.connect("BBDD I/PrimeraBase")
miCursor = miConexion.cursor()

# AGREGAR REGISTRO MEDIANTE UNA TUPLA

#variosProductos=[
#    ("Camiseta", 10, "Deportes"),
#    ("Jarron", 30, "Ceramica"),
#    ("Camion", 20, "Jugueteria")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

# HACER UNA LECTURA A LA BASE DE DATOS

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
#print(variosProductos)
for productos in variosProductos:
    print(productos)

miConexion.commit()
miConexion.close()
