# Decoradores II

def funcion_decoradora(funcion_parametro):

    # *args: puede recibir un numero indeterminado de paramatros
    # **kwargs: parametros 
    def funcion_interior(*args,  **kwargs): 

        # Acciones adicionales que decoran    
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro(*args,  **kwargs)

        #Acciones adicionale que decoran
        print("Hemos termiando el calculo")

    return funcion_interior



@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1+num2)

@funcion_decoradora
def multiplicacion(num1, num2):
    print(num1*num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))

suma(7,5)
resta(12,10)
multiplicacion(5,5)

potencia(base=5,exponente=3)