class Carrito:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto, cantidad):

        for item in self.productos:
            if item['producto']['id'] == producto['id']:
                item['cantidad'] += cantidad  
                print(f"Se agregaron {cantidad} unidades de '{producto['nombre']}' al carrito.")
                return
        
        self.productos.append({"producto": producto, "cantidad": cantidad})
        print(f"Se agregaron {cantidad} unidades de '{producto['nombre']}' al carrito.")

    def eliminar_producto(self, id_producto, cantidad):
        for item in self.productos:
            if item['producto']['id'] == id_producto:
                if cantidad >= item['cantidad']:
                    self.productos.remove(item)
                    print(f"Se eliminó completamente '{item['producto']['nombre']}' del carrito.")
                else:
                    item['cantidad'] -= cantidad
                    print(f"Se eliminaron {cantidad} unidades de '{item['producto']['nombre']}' " +
                        f"del carrito.")
                return
        print(f"No se encontró ningún producto con ID {id_producto} en el carrito.")

    def ver_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for item in self.productos:
                producto = item['producto']
                cantidad = item['cantidad']
                print(f"{producto['id']}: {producto['nombre']} - ${producto['precio']} x " +
                      f"{cantidad} = ${producto['precio'] * cantidad}")

    def calcular_total(self):
        return sum(item['producto']['precio'] * item['cantidad'] for item in self.productos)