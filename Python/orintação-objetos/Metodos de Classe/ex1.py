# 1. Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação 
# personalizada com base na profissão da pessoa.

class Pessoa:
    
    def __init__(self, nome, idade, profissao):
        self._nome      = nome  
        self._idade     = idade
        self._profissao = profissao
        
    def __str__(self):
        return f'Nome: {self._nome}, Idade: {self._idade}, Profissão: {self._profissao}'
    
    def aniversario(self):
        self._idade += 1
      
    def saudacao(self):
        if (self._profissao == 'Analista'):
            print('Analista - Mundo Tech em 2024!')
        else:
            print('Apenas Analista possuem mensagem!')
    
    
wesley      = Pessoa('Vieira', 20, 'Analista')
geovanna    = Pessoa('Moura', 22, 'Desenvolvedora')

print("\nInformações da Pessoa:")
print(wesley)
print(geovanna)

print('\nInformações da Pessoa após seu aniversário:')
wesley.aniversario()
geovanna.aniversario()
print(wesley)
print(geovanna)

print('\nMensagem da sua Profissião:')
wesley.saudacao()
geovanna.saudacao()
print()