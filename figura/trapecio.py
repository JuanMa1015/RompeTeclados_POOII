from figura import figura

class trapecio (figura):
    def __init__(self,color,nombre,base_mayor,base_menor,lado1,lado2):
        super().__init__(color,nombre)
        base_mayor  = base_mayor
        base_menor = base_menor
        lado1 = lado1
        lado2 = lado2
    
    def calcular_perimeto(self,base_mayor,base_menor,lado1,lado2):
        perimetro = base_menor + base_mayor + lado1 + lado2
        print (f"el perimetro del traapecio es {perimetro}")
        
    def calcular_area(self,base_mayor,base_menor,altura):
        altura = altura
        return (base_mayor + base_menor) * altura / 2
    
