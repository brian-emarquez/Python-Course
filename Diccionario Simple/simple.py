# Ejemplo de Diccionario Simple

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

# mueustra todo el diccionario
'''
for k,v in futbolistas.items():
    print ("%s -> %s" %(k,v))
'''
elem = futbolistas.get(6)
print ("\nObtenemos el valor cuya clave es '6' futbolistas.get(6): %s" %elem)