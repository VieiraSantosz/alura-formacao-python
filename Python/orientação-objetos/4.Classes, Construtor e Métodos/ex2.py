# 2. Na classe Livro, adicione um método especial str que retorna uma mensagem 
# formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da 
# classe Livro e imprima essas instâncias.

class Livro:
    
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo            = titulo
        self._autor             = autor
        self._ano_publicacao    = ano_publicacao
        self._disponivel        = True
        
    def __str__(self):
        return f'Titulo: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'
    

livro1 = Livro('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 2005)
livro2 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997)

print('\nInformações dos Livros:')
print(livro1)
print(livro2)
print()