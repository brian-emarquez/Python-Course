def imprimir():
    print("________________________")
    print("Bienvenido al Cajero")
    print("________________________")
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
            entrada_usuario = int(input("Seleccione una opcion: "))

            if entrada_usuario in range(5):

                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    break
                print()
                print("Usted eligió la opcion {} !\n".format(entrada_usuario))
            else:
                print('Error, solo de aceptan numeros del 0 al 4')

        except ValueError:
            print("Error, ingrese solamente numeros")


if __name__ == '__main__':
    menu()