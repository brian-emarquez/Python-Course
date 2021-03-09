### Lambda

En Python, una función Lambda se refiere a una pequeña función anónima. Las llamamos “funciones anónimas” porque técnicamente carecen de nombre.

Al contrario que una función normal, no la definimos con la palabra clave estándar def que utilizamos en Python. En su lugar, las funciones Lambda se definen como una línea que ejecuta una sola expresión. Este tipo de funciones pueden tomar cualquier número de argumentos, pero solo pueden tener una expresión.

```python
#Escribo p1 y p2 como parámetros 1 y 2 de la función.
lambda p1, p2: expresión 
```

Como mejor te lo puedo explicar es enseñándote un ejemplo básico, vamos a ver una función normal y un ejemplo de Lambda:

```python
#Aquí tenemos una función creada para sumar.
def suma(x,y):
    return(x + y)

#Aquí tenemos una función Lambda que también suma.
lambda x,y : x + y

#Para poder utilizarla necesitamos guardarla en una variable.
suma_dos = lambda x,y : x + y
```

## Aplicación de Lambdas

Quiero darte algunas ideas de dónde se podrían aplicar las Lambdas. A continuación he creado algunos ejemplos aplicando las Lambdas con diferentes objetivos. Así podras entender mejor como funcionan.

## Lambda en Pandas DataFrame con el método apply()

Se me ocurre que podemos aplicar una función Lambda a data cleaning en Pandas con el método apply(), algo que creo nos puede ser de utilidad para evitar crear un bucle que vaya recorriendo todo el DataFrame:
