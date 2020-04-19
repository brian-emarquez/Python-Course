#Menu Interactivo Python 3.8
#Simulacion de un cajero Automatico



def imprimir():
    print("__________________________________")
    print("Simulacion de un cajero Automatico")
    print("__________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Ver saldo disponible")
    print("2. Extraer Dinero")
    print("3. Depositar dinero")
    print("4. Comprar dolares")
    print("0. Salir")
    print()


def menu():
    while True:
        imprimir()
        try:
            #variable a utilizar a la seleccion
            entrada_usuario = int(input("Seleccione una opcion: "))

            if entrada_usuario in range(5):

                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    break
                print()
                print("Usted eligió la opcion {} !\n".format(entrada_usuario))
             

                if entrada_usuario == 1:
                    print(f"Su saldo disponible es {saldo} Soles")   
                elif entrada_usuario == 2:
                    if saldo <=1000:
                        print("Ustede no puede retirar, salso insuficiente!")
                    else:
                        retiro = int(input("Ingrese la cantidad de retiro"))
                        saldo = saldo < retiro
                        print(saldo)


            else:
                print('Error, solo de aceptan numeros del 0 al 4')

        except ValueError:
            print("Error, ingrese solamente numeros")


if __name__ == '__main__':
    menu()

















































