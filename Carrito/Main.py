from Carrito import Carrito
from Usuario import Usuario
from Cliente import Cliente
from Admin import Administrador
def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"{producto['id']}: {producto['nombre']} - ${producto['precio']}")

def main():

    productos_disponibles = [
        {"id": 1, "nombre": "Camiseta", "precio": 80000},
        {"id": 2, "nombre": "Baggy", "precio": 135000},
        {"id": 3, "nombre": "Gorra", "precio": 55000},
        {"id": 4, "nombre": "Gafas", "precio": 95000},
        {"id": 5, "nombre": "Zapatos", "precio": 220000},
    ]

    carrito = Carrito()
    

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    tipo_usuario = input("Ingrese su rol")

    if tipo_usuario == "Administrador":
        cliente = None
        admin = Administrador(nombre, edad)
    else:
        admin = None
        cliente = Cliente(nombre, edad)


    usuario = Usuario(nombre, edad)

    while True:
        print("\n--- Menú ---")
        print("1. Ver productos disponibles")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Ver carrito")
        print("5. Finalizar compra")
        print("6. Salir")
        print("7. Mostrar información usuario")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos(productos_disponibles)

        elif opcion == "2":
            mostrar_productos(productos_disponibles)
            id_producto = int(input("Ingrese el ID del producto que desea agregar: "))
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            producto = next((p for p in productos_disponibles if p['id'] == id_producto), None)
            if producto:
                carrito.agregar_producto(producto, cantidad)
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
            cantidad = int(input("Ingrese la cantidad de unidades que quiere a eliminar: "))
            carrito.eliminar_producto(id_producto, cantidad)

        elif opcion == "4":
            carrito.ver_carrito()

        elif opcion == "5":
            total = carrito.calcular_total()
            total_con_descuento = usuario.aplicar_descuento(total)
          
            if edad  >= 41 and edad <= 60:
                print("No tienes derecho a descuento, por ser estar entre los 41 y 60 años de edad.")
                print(f"\nTotal: ${total}")

            else:
                print(f"\nTotal sin descuento: ${total}")
                print(f"Total con descuento: ${total - total_con_descuento}")
            break

        elif opcion == "6":
            print("Gracias por visitarnos. ¡Hasta luego!")
            break
        elif opcion == "7":

            if cliente:
                cliente.mostrar_informacion()

            if admin:
                admin.mostrar_informacion()

          
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()