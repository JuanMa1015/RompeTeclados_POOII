class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
        for e in self.empleados:
            print(e)

    def buscar_salario(self, nombre):
        for e in self.empleados:
            if e.nombre.lower() == nombre.lower():
                print(f"El salario de {e.nombre} es: {e.salario_total}")
                return
        print("Empleado no encontrado")
