# Decoradores I
# funciones decoreadores (A,B,C)

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        # Acciones adicionales que decoran    
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro()

        #Acciones adicionale que decoran
        print("Hemos termiando el calculo")

    return funcion_interior



@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()