"""
Estraer Json
"""

datos_JSON =  """
{
    "tamano": "mediana",
    "precio": 15.67,
    "toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
    "cliente": {
        "nombre": "Brian Marquez",
        "telefono": "696969669696",
        "correo": "brian@mail.com"
    }
}
"""
# Convertir cadena de caracteres JSON a un diccionario
data_dict = json.loads(datos_JSON)

print(data_dict["tamano"])