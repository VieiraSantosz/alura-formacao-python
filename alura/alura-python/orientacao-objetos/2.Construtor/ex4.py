# 4. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria 
# como parâmetros e inicia ativo como False por padrão. 
# Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, endereco, classificacao):
        self.nome            = nome
        self.categoria       = categoria
        self.ativo           = False
        self.endereco        = endereco
        self.classificacao   = int(classificacao)
    
outbakc = Restaurante('Outback Tatuapé', 'Steakhouse', 'R. Gonçalves Crespo, 78', 4)

print(f'\nRestaurante - {outbakc.nome} | {outbakc.categoria} | {outbakc.ativo} | {outbakc.endereco} | {outbakc.classificacao}\n')