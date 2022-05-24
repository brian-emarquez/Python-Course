print('Proporcione lo siguientes datos del libro: ')
nombre = input('proporciona el nombre del libro: ')
id = int(input('proporciona el precio del libro: '))
precio = float(input('proporciona el valor del libro: '))
envioGratuito = bool(input('si es envio gratuito (True/False): '))

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito =='False':
    envioGratuito = False
    
else:
    envioGratuito = "Valor incorrecto, debe escribir True o False"

# imprimir los datos
print(f'''
      Nombre : {nombre}, 
      id: {id},
''')
