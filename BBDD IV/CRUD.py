# CRUD

import sqlite3

miConexion = sqlite3.connect("BBDD IV/GestionProductos")
miCursor = miConexion.cursor()

# READ - LECTURA
#miCursor.execute("SELECT * from PRODUCTOS WHERE SECCION='Confeccion'")

#productos=miCursor.fetchall()
#print(productos)


# Update - ACTUALIZACION
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO='40' WHERE  NOMBRE_ARTICULO='Peleta'")

# DELETE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")


miConexion.commit()
miConexion.close()
