edad = int(input('Ingrese su edad: '))

mensaje = " " #None
print('---->', mensaje)
if 0 < edad < 10:
    mensaje = 'la infancia es increible'
print(f'Tu Edad es: {edad}, {mensaje}')