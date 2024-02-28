# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from livro import Livro

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar 
# e imprima se o livro está disponível ou não após o empréstimo.

livro1 = Livro('Velozes e Furiosos', 'Paul Walker', 2003)
livro1.emprestar()

def main():
    print(f'\nStatus do Livro: {livro1.estado_livro}\n')


if __name__ == '__main__':
    main()