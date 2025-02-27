
class Empleado:
    def __init__(self, nombre, edad, cargo, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario_base = salario_base
        self.salario_total = self.definir_salario()

    def definir_salario(self):
        if self.cargo == "Gerente":
            return self.salario_base + 500
        elif self.cargo == "Desarrollador":
            return self.salario_base + 300
        elif self.cargo == "Diseñador":
            return self.salario_base + 200
        else:
            return self.salario_base

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Cargo: {self.cargo}, Salario: {self.salario_total}"