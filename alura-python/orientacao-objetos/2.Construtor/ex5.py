# 5. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
# seja exibida uma mensagem formatada com o nome e a categoria. 
# Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, endereco, classificacao):
        self.nome            = nome
        self.categoria       = categoria
        self.ativo           = False
        self.endereco        = endereco
        self.classificacao   = int(classificacao)
        
    def __str__(self):
        return f'Restaurante - {self.nome} | {self.categoria} | {self.ativo} | {self.endereco} | {self.classificacao}'
    
outbakc = Restaurante('Outback Tatuapé', 'Steakhouse', 'R. Gonçalves Crespo, 78', 4)

print(outbakc)