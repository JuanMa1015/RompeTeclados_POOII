from figura import Figura
from math import pi

class Circulo(Figura):
    def __init__(self, color, nombre, area):
        super().__init__(color, nombre)
        self.area = area
        self.pi = pi
    
    def get_nombre(self): #get - obtener
        return self._nombre
    
    def calcular_area(self, area):
        area = pi * (area ** 2)
        print(f"el área del circulo es: {area:.2f}") 
    
    def calcular_perimetro(self, area):
        perimetro = 2 * pi * area
        print(f"el perímetro del circulo es: {perimetro:.2f}")
