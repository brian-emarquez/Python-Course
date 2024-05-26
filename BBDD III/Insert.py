# Insert 
import sqlite3

miConexion = sqlite3.connect("BBDD III/GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tran', 15, 'jugueteria')")

miConexion.commit()
miConexion.close()
