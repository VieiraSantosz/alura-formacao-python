# 4. Adicione um método estático chamado verificar_disponibilidade à classe 
# Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

class Livro:
    lista_livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo            = titulo
        self._autor             = autor
        self._ano_publicacao    = ano_publicacao
        self._disponivel        = True
        
        Livro.lista_livros.append(self)
        
    def __str__(self):
        return f'Titulo: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao} | Estado: {self.estado_livro}'
    
    def emprestar(self):
        self._disponivel = False
         
    @property
    def estado_livro(self):
        return 'Disponível' if self._disponivel else 'Indisponivel'
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livro_encontrado = False
        
        for livro in Livro.lista_livros:
            
            if (livro._ano_publicacao == ano and livro._disponivel == True):
                livro_encontrado = True
                print(f'Livro: {livro._titulo.ljust(40)} | Status: {livro.estado_livro}')
                
        if (not livro_encontrado):
            print(f'Nenhum Livro Disponivél com o ano {ano}')
                

livro1 = Livro('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', 2005)
livro2 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997)
livro3 = Livro('O Senhor dos Anéis: A Sociedade do Anel', 'Tolkien', 2005)

Livro.verificar_disponibilidade(200)