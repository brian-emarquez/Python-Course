#FUNCIONES - DEF()
#print()
#dir()
#type()

def hello(name):
    print("Hola "+ name)

hello("brian") #llamada a la funcion
 
print("---------------------------------------------------")
def hola(variable):
    print("vemos una variable: " + variable)

hola("Carro")
hola("ventana")
hola("lapiz")

print("---------------------------------------------------")

def hola1(nombres="Yuliza"):# imprime el nombre si en la llamada esta vacio
    print("los nobes son: " + nombres)

#hola1("brian")# lamada vacio
hola1()# lamada vacio

print("---------------------------------------------------")

def suma (numero1, numero2):
    print(numero1 + numero2)

suma(10, 10)
suma(100, 50)
suma(75, 50)


print("---------------------------------------------------")

def suma1 (numero1, numero2):
    return(numero1 + numero2)

print(suma1(10, 10))
print(suma1(100, 50))
print(suma1(75, 50))


