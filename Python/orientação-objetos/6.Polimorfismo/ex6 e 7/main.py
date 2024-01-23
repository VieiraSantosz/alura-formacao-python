# 6. Em um arquivo chamado main.py, importe a classe Carro.

from carro import Carro


# 7. No arquivo main.py, instancie três objetos da classe Carro com diferentes 
# características, como marca, modelo e cor.

mercedes    = Carro('Mercedes', 'A45', 'Prata')
ferrari     = Carro('Ferrari', 'La Ferrari', 'Vermelho')
ford        = Carro('Ford', 'Mustang', 'Branco')


def main():
    print('\nLista de Carros:')
    print(mercedes)
    print(ferrari)
    print(ford)
    print()
    
if __name__ == '__main__':
    main()