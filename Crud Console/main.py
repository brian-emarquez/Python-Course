from os import system
import time
import conexion as conn
db = conn.DB()
system("clear")

def create():
    name = str(input("INGRESA SU NOMBRE: "))
    email = str(input("INGRESA SU EMAIL: "))
    if(len(name) > 0 and len(email) > 0):
        sql = "INSERT INTO sistema(name,email) VALUES(?,?)"
        parametros = (name,email)
        db.ejecutar_consulta(sql,parametros)
        print("Insertados")

def read():
    sql = "SELECT * FROM sistema"
    result = db.ejecutar_consulta(sql)
    for data in result:
        print(""" 
        ID :        {}
        NOMBRE :    {}
        EMAIL :     {}
        """.format(data[0],data[1],data[2]))

def update():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        name = str(input("INGRESA SU NOMBRE: "))
        email = str(input("INGRESA SU EMAIL: "))
        if(len(name) > 0 and len(email) > 0):
            sql = "UPDATE sistema SET name=?,email=? WHERE id=?"
            parametros = (name,email,id)
            db.ejecutar_consulta(sql,parametros)
            print("Actualizado!")
    else:
        print("Se require un ID")

def delete():
    id = int(input("INGRESA EL ID: "))
    if(id != 0):
        sql = "DELETE FROM sistema WHERE id=?"
        parametros = (id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eliminado!")
    else:
        print("Se require un ID")
        
def search():
    nombre = str(input("Buscar por nombre: "))
    if(len(nombre) > 0):
        sql = "SELECT * FROM sistema WHERE name LIKE ?"
        parametros = ('%{}%'.format(nombre),)
        result = db.ejecutar_consulta(sql,parametros)
        for data in result:
            print(""" 
            +ID :        {}
            +NOMBRE :    {}
            +EMAIL :     {}""".format(data[0],data[1],data[2]))
while True:
    print("=========================================")
    print("\tCRUD CON SQLite3")
    print("=========================================")
    print("\t[1] Insertar registro")
    print("\t[2] Listar registros")
    print("\t[3] Actualizar registros")
    print("\t[4] Eliminar registros")
    print("\t[5] Buscar registros")
    print("\t[6] Salir")
    print("=========================================")

    try:
        opcion = int(input("Selecciona una opcion: "))
        if(opcion == 1):
            create()
            time.sleep(1)
            system("clear")
        elif (opcion == 2):
            read()
            time.sleep(1)
        elif (opcion == 3):
            update()
            time.sleep(1)
            system("clear")
        elif (opcion == 4):
            delete()
            time.sleep(1)
            system("clear")
        elif (opcion == 5):
            search()

        elif (opcion == 6):
            break
    except:
        print("Por favor, selecciona las opciones correctas")
        system("clear")
