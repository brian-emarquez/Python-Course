# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento (key)
print( diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
