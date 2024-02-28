# 8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. 
# Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, 
# quantidade de portas e tipos.

from carro import Carro
from moto  import Moto

mercedes = Carro('Mercedes', 'A45', 4)
bmw      = Carro('Bmw', 'X6', 4)
ferrari  = Carro('Ferrari', 'Enzo', 2)

honda  = Moto('Honda', 'Hornet', 'Esportiva')
yamaha = Moto('Yamaha', 'Xt 660r', 'Esportiva')
harley = Moto('Harley', 'Roadter 1200', 'Casual')


# 9. Exiba as Informações: Para cada instância, imprima no console as 
# informações utilizando o método str.

def main():
    print('\nInformações dos Carros listados:')
    print(mercedes)
    print(bmw)
    print(ferrari)
    
    print('\nInformações das Motos listadas:')
    print(honda)
    print(yamaha)
    print(harley)
    

if __name__ == '__main__':
    main()