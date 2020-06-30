# Metod de Cadenas 2

# Metodos de Cadenas
# Metodos para manipular cadenas
# Numeros

edad=input("Introduce su edad: ")

while (edad.isdigit()==False):
    print("vuelva a ingresar")
    edadUsuario=input("Introduce su edad: ")

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes Pasar")
5