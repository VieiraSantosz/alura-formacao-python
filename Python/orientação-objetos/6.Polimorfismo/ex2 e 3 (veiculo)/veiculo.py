# 2. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

from abc import ABC, abstractstaticmethod

class Veiculo(ABC):
    
    @abstractstaticmethod
    def ligar(self):
        pass
    

# 3. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

    def __init__(self, marca, modelo):
        self._marca  = marca
        self._modelo = modelo
        
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo}'