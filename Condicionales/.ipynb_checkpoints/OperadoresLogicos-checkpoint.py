#Operadores Logicos
#and = El operador and evalúa si el valor del lado izquierdo y el lado derecho se cumple.
#or = El operador or evalúa si el valor del lado izquierdo o el lado derecho se cumple.
#not = El operador not devuelve el valor opuesto la valor booleano.

#x = 5
#y = 6
x = int(input("ingrese un numero: "))
y = int(input("ingrese un numero: "))

if x > 2 and y <= 10:
    print ("1 opcion - x es mayor que 2 y x es menor igual 10 ")
else:
    print ("no se puede ejecutar la 1 opcion")

if x > 2 or y <= 10:
    print ("2 Opcion - x es mayor que 2 o x es menor igual que 10")
else:
    print ("no se puede ejecutar la 2 opcion")

if (not( x==y )):
    print("3 opcion - x no es igual que y")
else:
    print ("no se puede ejecutar la 3 opcion")