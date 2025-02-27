from abc import ABC
from abc import abstractmethod

class Figura(ABC):
    def __init__(self, color, nombre):
        self.__color = color
        self.__nombre = nombre 
        
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass




