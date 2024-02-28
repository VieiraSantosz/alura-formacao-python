from modelos.restaurante        import Restaurante
from modelos.cardapio.bebida    import Bebida
from modelos.cardapio.prato     import Prato

restaurante_praça   = Restaurante('praça', 'gourmet')
suco                = Bebida('Suco de Uva', 5.0, 'Grande')
paozinho            = Prato('Paozinho', 2.0, 'O melhor da cidade')

suco.aplicar_desconto()
paozinho.aplicar_desconto()

restaurante_praça.adicionar_no_cadarpio(suco)
restaurante_praça.adicionar_no_cadarpio(paozinho)



def main():
    restaurante_praça.exibir_cardapio

if __name__ == '__main__':
    main()