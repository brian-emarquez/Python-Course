#Utilizamos If con String

color = "red"
#color = input("Ingrese un color: ") 

if color == "blue":
    print ("es color  es blue")
elif color == "red":
    print("es color es red")
else: 
    print ("es otro color")

print("===============================================================")

name = "jhon"
lastname= "carter"
#name = input("ingrese un nombre: ")
#lastname = input("Ingrese un apellido: ")
if name =="jhon":
    if lastname=="carter": # condicionales anidadas
        print("tu eres jhon carter")
    else:
        print(" tu no eres jhon carter")
else:
    print(" tu no eres jhon carter")

print("===============================================================")
