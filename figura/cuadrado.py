from figura import Figura

class Cuadrado(Figura):
    def __init__(self, color, nombre, lado1):
        super().__init__(color, nombre )
        self.lado1 = lado1
    
    def get_nombre(self): #get - obtener
        return self._nombre
    
    def calcular_area(self, lado1):
        area = lado1 ** 2
        print(f"el área del cuadrado es: {area:.2f}") 
    
    def calcular_perimetro(self, lado):
        perimetro = lado * 4
        print(f"el perímetro del cuadrado es: {perimetro:.2f}")