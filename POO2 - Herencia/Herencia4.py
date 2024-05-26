# Herencia 4
# Super

class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self. edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado ,residencia_empleado) #llama a metodo de la case padre

        self.salario = salario
        self.antiguedad = antiguedad

#Obejetos
Objeto=Empleado(1500, 15, "Manuel", 55 , "Peru")
Objeto.descripcion()

