# BBDD I
# Coneccion con base de datos
# SGDB
# Sql server, Oracle, Mysql, SQLITE, PostSQL, etc

# Module Imports
# import mariadb
# import sys

import sqlite3

miConexion = sqlite3.connect("BBDD I/PrimeraBase")
miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
miConexion.commit()

miConexion.close()
