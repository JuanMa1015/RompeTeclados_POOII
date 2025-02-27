from empleado import Empleado
from empresa import Empresa

def agregar_empleado(empresa):
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad: "))
    cargo = input("Cargo (Gerente, Desarrollador, Diseñador): ")
    salario_base = float(input("Salario base: "))

    nuevo_empleado = Empleado(nombre, edad, cargo, salario_base)
    empresa.agregar_empleado(nuevo_empleado)

def mostrar_empleados(empresa):
    empresa.mostrar_empleados()

def calcular_salario(empresa):
    nombre = input("Ingrese el nombre del empleado: ")
    empresa.buscar_salario(nombre)

def main():
    empresa = Empresa()
    while True:
        print("\n1. Agregar empleado\n2. Mostrar empleados\n3. Calcular salario\n4. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            agregar_empleado(empresa)
        elif opcion == 2:
            mostrar_empleados(empresa)
        elif opcion == 3:
            calcular_salario(empresa)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()