#Excepciones 3
#Excepcion dentro de una funcion

def divide ():
    
    try:
        op1=(float(input("Introduce el primer Numero: ")))
        op2=(float(input("Introduce el segundo Numero:                                                                         ")))

        print("La Division es: " +str(op1/op2))

    except ValueError:
        print("Caracteres no aceptados")

    except ZeroDivisionError:
        print("No se aceptar divicion entrer 0")

    finally:
        print("Calculo finalizado")#siempre se ejecutara

divide()


