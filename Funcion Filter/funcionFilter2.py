# FUNCIONES FILTER
# PROGRAMACION FUNCIONAL (PARADIGMA)

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que traba como  {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
    Empleado("juan","Director",750000),
    Empleado("brian","presidenta",580000),
    Empleado("Antonio","Acminitrativo",25000),
    Empleado("sara","Secretaria",27000),
    Empleado("Mario","Botones",21000)
]

salario_altos=filter(lambda empleado: empleado.salario>50000, listaEmpleados)

for empleado_Salario in salario_altos:
    print(empleado_Salario)

