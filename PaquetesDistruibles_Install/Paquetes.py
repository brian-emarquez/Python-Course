# Paquetes

#Son directorios donde se almacenaran modulos relacionados entre si
#y sirven para organizar y reutilizar los modulos
#nos vinculamos a la carpeta Calculos y al archivo CalculoGenerales.py

from Calculos.CalculoGenerales import dividir
from Calculos.OperacionBasica.Operacion_Basica import sumar
from Calculos.RedondeaPotencia.Redondea_Potencia import redondear


dividir(100, 15)
sumar(50, 50)
redondear(5.9)

