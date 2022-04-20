from calendar import prmonth


class Persona:
    
    #mi_Atributo = ""
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    """def __str__(self):
        pass
    
    def __repr__(self):
        pass"""
    
persona1 = Persona("brian", "gonzalez", 23)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
