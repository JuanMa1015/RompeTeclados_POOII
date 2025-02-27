class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def aplicar_descuento(self, total):
        #Menor que 25 años, no incluye el 25. DESCUENTO 10%
        if self.edad < 25:
            return total * 0.1  
        #Entre 26 y 40 años, incluye el 26 y 40. DESCUENTO 15%
        elif self.edad >=26 and self.edad <= 40 :
            return total * 0.15 
        #Mayor que 40 años y menor que 60 años, incluye el 41 y 60. NO DESCUENTO 
        elif self.edad >= 41 and self.edad <= 60:
            return total
        #Mayor que 60 años, no incluye el 60. DESCUENTO 30%
        else:
            return total * 0.3

    def mostrar_informacion(self):
        return print(f"{self.nombre} su edad es : {self.edad}")