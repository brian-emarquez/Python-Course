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
print(f"persona  1: ", {persona1})
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 =  Persona("kike", "clavijo", 30)
print(f'persona  2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
