#Example Python (FOR 3)
print("============================================================================")
veces = 4
#veces = int(input("¿Cuántas veces quieres que te hola? "))

for i in range(veces):
    print("Hola ", end="")
print()
print("Adiós")

print("============================================================================")
print("Comienzo")
cuenta = 0
for i in range(1, 6):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")

print("============================================================================")
print("Comienzo")
encontrado = False
for i in range(1, 6):
    if i % 2 == 0:
        encontrado = True
if encontrado:
    print(f"Entre 1 y 5 hay al menos un múltiplo de 2.")
else:
    print(f"Entre 1 y 5 no hay ningún múltiplo de 2.")