from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo

def main():
    circulo = Circulo("Rojo","Circulito", 23)
    circulo.calcular_area(circulo.area)
    circulo.calcular_perimetro(circulo.area)    
    print("\n")

    cuadrado = Cuadrado("Azul","Cuadradito", 15)
    cuadrado.calcular_area(cuadrado.lado1)
    cuadrado.calcular_perimetro(cuadrado.lado1)
    print("\n")
    
    rectangulo = Rectangulo("Verde","Rectangulito", 67, 80)
    rectangulo.calcular_area(rectangulo.base, rectangulo.altura)
    rectangulo.calcular_perimetro(rectangulo.base, rectangulo.altura)

if __name__ == "__main__":
    main()