#Diccionarios

equipo = {
	10: "Paulo Divala",
	11: "Luis Medina",
	12: "Carlos Miranda",
	13: "Erick Cruz",
}

print()
print(equipo)
print(equipo[10])
print(equipo[11])

# Si no existe el Numero

print(equipo.get(6,"no exixte ese jugador"))

# si se encuentra en el equipo

print(11 in equipo)

# cuantos hay en el equipo

print(len(equipo))

#Eliminar todo el equipo

equipo.clear()
print(equipo)