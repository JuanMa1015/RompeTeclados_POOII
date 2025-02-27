from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

        self.tipo_membresia = 'Cliente'
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        return print(self.tipo_membresia)
        # return print(f"{self.nombre} su edad es : {self.edad} y su membresia es: {self.tipo_membresia}")
