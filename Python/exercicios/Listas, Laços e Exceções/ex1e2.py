# 1. Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes   = ['Vieira', 'Geovanna', 'Marco', 'Luiza']
anos    = [2002, 2024]


# 2 - Crie uma lista e utilize um loop for para percorrer todos 
# os elementos da lista

def lista_numeros():
    print('\nLista de Números:')
    for numero in numeros:
        print(numero)
    
def lista_nomes():
    print('\nLista de Nomes:')
    for nome in nomes:
        print(nome)
        
def lista_anos():
    print('\nLista de Anos:')
    for ano in anos:
        print(ano)
        

def main():
    lista_numeros()
    lista_nomes()
    lista_anos()
    
if __name__ == '__main__':
    main()