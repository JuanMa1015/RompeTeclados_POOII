from figura import Figura

class Rectangulo(Figura):
    def __init__(self, color, nombre, base, altura):
        super().__init__(color, nombre)
        self.base = base
        self.altura = altura
    
    def get_nombre(self): #get - obtener
        return self._nombre
    
    def calcular_area(self, base, altura):
        area = base * altura
        print(f"el área del rectangulo es: {area:.2f}") 
    
    def calcular_perimetro(self, base, altura):
        perimetro = 2 * (base * altura)
        print(f"el perímetro del rectangulo es: {perimetro:.2f}")