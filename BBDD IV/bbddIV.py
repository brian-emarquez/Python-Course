# BBDDD IV
# Clausula UNIQUE -no se puede repetir el registro
# OPERACIONES CRUD



import sqlite3

miConexion = sqlite3.connect("BBDD IV/GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[

    ("Peleta", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()
miConexion.close()
