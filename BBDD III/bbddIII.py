# BBDDD III
# 


import sqlite3

miConexion = sqlite3.connect("BBDD III/GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[

    ("AR01", "Peleta", 20, "Jugueteria"),
    ("AR02", "Pantalon", 15, "Confeccion"),
    ("AR03", "Destornillador", 25, "Ferreteria"),
    ("AR04", "Jarron", 45, "Ceramica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)


miConexion.commit()
miConexion.close()
