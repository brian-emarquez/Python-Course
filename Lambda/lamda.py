#Importo pandas y numpy para crear un DataFrame
import pandas as pd
import numpy as np

#Creo un DataFrame con dos columnas, Celsius y Kelvin, ambas con datos iguales
data = {'Celsius':[22, 36, 20, 26, 30, 38],
        'Kelvin':[22, 36, 20, 26, 30, 38]}

#Creo el DataFrame con el su index y las columnas Celsius y Kelvin
df = pd.DataFrame(data, index = ['Londres','Madrid','Barcelona','Sevilla','Cádiz','Lima'])

#Creo una función Lambda para pasar los grados Celsius a Kelvin.
to_kelvin = lambda x: (x + 273,15)

#Aplico la Lambda a la columna [Kelvin] con el método apply()
df = df['Kelvin'].apply(to_kelvin)

print(df)