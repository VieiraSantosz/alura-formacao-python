# 8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, 
# instancie dois objetos da classe Livro e exiba a mensagem 
# formatada utilizando o método str.

from livro import Livro

livro1 = Livro('Homem Aranha', 'Tobey Maguire', 2005)
livro2 = Livro('Batman, Cavaleiro das Trevas', 'Christian Bale', 2009)

def main():
    print(livro1)
    print(livro2)
    
if __name__ == '__main__':
    main()