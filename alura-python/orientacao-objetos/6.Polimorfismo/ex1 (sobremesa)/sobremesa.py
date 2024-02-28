# 1. Crie uma classe chamada Sobremesa que herda de ItemCardapio, adicione dois atributos 
# específicos como tipo e tamanho, à classe Sobremesa. 

# Atualize o método __str__ conforme necessário para refletir essas mudanças.

# Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio.

from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo    = tipo
        self.tamanho = tamanho
        
    def __str__(self) -> str:
        return super().__str__() + f' | Tipo: {self.tipo} | Tamanho: {self.tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)
        

sorvete = Sobremesa('Sorvete', 100, 'Flocos', 'Grande')

def main():
    print('\nInformações do Sorvete antes do desconto:')
    print(sorvete)

    sorvete.aplicar_desconto()
    print('\nInformações do Sorvete depois do desconto:')
    print(sorvete)
    print()
    
if __name__ == '__main__':
    main()