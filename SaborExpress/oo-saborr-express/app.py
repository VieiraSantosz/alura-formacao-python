from modelos.restaurante import Restaurante

restaurante_praça = Restaurante('praça', 'gourmet')
restaurante_praça.receber_avaliacao('Vieira', 5)


def main():
    Restaurante.exibir_restaurante()

if __name__ == '__main__':
    main()