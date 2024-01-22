from abc import ABC, abstractstaticmethod

class Veiculo(ABC):
    
    @abstractstaticmethod
    def ligar(self):
        pass

    def __init__(self, marca, modelo):
        self._marca  = marca
        self._modelo = modelo
        
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo}'