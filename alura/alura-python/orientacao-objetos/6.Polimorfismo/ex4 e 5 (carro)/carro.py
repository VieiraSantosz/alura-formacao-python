# 4. Crie uma nova classe chamada Carro que herda da classe Veiculo.

# 5. No construtor da classe Carro, utilize o método super() para chamar o 
# construtor da classe pai e atribua o atributo específico cor à classe filha.

from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
    def __str__(self):
        return super().__str__() + f' | Cor: {self.cor}'
    
    def ligar(self):
        pass