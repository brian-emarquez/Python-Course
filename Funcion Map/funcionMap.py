# Funcion Map
# Aplica una funcion a cada elemento de una lista iterable

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que traba como  {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

    Empleado("juan","Director",6700),
    Empleado("brian","presidenta",7500),
    Empleado("Antonio","Acminitrativo",2100),
    Empleado("sara","Secretaria",2150),
    Empleado("Mario","Botones",1800)
]

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03

    return empleado

listaEmpleadoComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadoComision:
    print(empleado)