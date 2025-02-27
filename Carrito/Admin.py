from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

        self.permisos = [
            "Editar",
            "Eliminar",
            "Actualizar",
            "Crear"
        ]
    
    def mostrar_informacion(self):
        return print(f"{self.nombre} su edad es : {self.edad} y sus permisos son: {self.permisos}")