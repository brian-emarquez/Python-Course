# edades

edad = int(input("Introduce tu edad: "))

veintes = edad  >= 18 and edad < 30
print(veintes)
treintas = edad >= 20 and edad < 40
print(veintes)


if veintes or treintas:
    print(f"dentro del rango")
else:
    print("no estas en el rango")
