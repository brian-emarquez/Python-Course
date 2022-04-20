# funcion recursiva
# funcion que se llama asi misma para ejecutar una operacion (factortorial)

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 5
resultado = factorial(numero)

print(f'El factorial de {numero} es {resultado}')




