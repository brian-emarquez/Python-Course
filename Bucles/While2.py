# While 2
i=1
while i <=10:
    print("Ejecucion " + str(i))
    i=i+1

print("Termino la Ejecucion")

#=====================================================================
# While Edades
edad=  int(input("Ingrese su Edad: "))

while edad <=0 or edad>=100:
    print("\nEdad Incorrecta!")
    edad=  int(input("Ingrese nuevamente su edad: "))

edad= input(f".:Edad Aceptada:. ---> {edad}")


