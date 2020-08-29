
# CONECTAR CON MARIADB
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

# CONECTAR CON SQL SERVER
#conn = pyodbc.connect(
#
#    "Driver={SQL Server Native Client 11.0};"
#    "Server=DESKTOP-URCHNPM;"
#    "Database=test;"
#    "password=briandb;"
#    "Trusted_Connection=yes;"
#)

