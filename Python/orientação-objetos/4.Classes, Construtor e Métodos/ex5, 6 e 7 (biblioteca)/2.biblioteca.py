# 7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade 
# para obter a lista de livros disponíveis publicados em um ano específico.

from livro import Livro

livro1 = Livro('Velozes e Furiosos', 'Paul Walker', 2003)
livro2 = Livro('Tokyo Drif', 'Vin Diesel', 2003)
livro3 = Livro('Operação Rio', 'Michelle Rodriguez', 2003)


def main():
    Livro.verificar_disponibilidade(2003)


if __name__ == '__main__':
    main()