# 3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo 
# disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima 
# se o livro está disponível ou não.

class Livro:
    
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo            = titulo
        self._autor             = autor
        self._ano_publicacao    = ano_publicacao
        self._disponivel        = True
        
    def __str__(self):
        return f'Titulo: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao} | Estado: {self.estado_livro}'
    
    def emprestar(self):
        self._disponivel = False
         
    @property
    def estado_livro(self):
        return 'Disponível' if self._disponivel else 'Indisponivel'
    

livro1 = Livro('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 2005)
livro1.emprestar()
livro2 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997)

print('\nInformações dos Livros:')
print(livro1)
print(livro2)
print()