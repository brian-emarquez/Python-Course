# BBDD I
# Coneccion con base de datos
# SGDB
# Sql server, Oracle, Mysql, SQLITE, PostSQL, etc

# Module Imports
#import mariadb
#import sys

# Connect to MariaDB Platform
#try:
#    conn = mariadb.connect(
#        user="briandb",
#        password="briandb",
#        host="127.0.0.1",
#        port=3307,
#        database="test2"
#    )
    
#except mariadb.Error as e:
#    print(f"Error connecting to MariaDB Platform: {e}")
#    sys.exit(1)

# Get Cursor
#cur = conn.cursor()

import mariadb
import sys

mariadb_conexion = mariadb.connect(host='127.0.0.1', port=3307, user='briandb', password='briandb', database='test2')
cursor = mariadb_conexion.cursor()
try:
    cursor.execute("SELECT ID,USERNAME,PASSWORD,NOMBRE FROM Usuarios")
    for id_usuario, username, password, nombre in cursor:
        print("id: " + str(id_usuario))
        print("username: " + username)
        print("password: " + password)
        print("nombre: " + nombre)
except mariadb.Error as error:
    print("Error: {}".format(error))
mariadb_conexion.close()