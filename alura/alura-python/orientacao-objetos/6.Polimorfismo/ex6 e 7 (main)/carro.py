from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
    def __str__(self):
        return super().__str__() + f' | Cor: {self.cor}'
    
    def ligar(self):
        pass