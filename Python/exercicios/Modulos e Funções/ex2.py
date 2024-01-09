# 2. Pergunte ao usuário sua idade e, com base nisso, use uma 
# estrutura if elif else para classificar a idade em categorias 
# de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def idade_categoria():
    
    idade = int(input('\nDigite sua idade: '))

    if (0 <= idade <= 12):
        print(f'\nCategoria Criança - {idade} anos.\n')
        
    elif (13 <= idade <= 18):
        print(f'\nCategoria Adolescente - {idade} anos.\n')
        
    elif (idade > 18):
        print(f'\nCategoria Adulto - {idade} anos.\n')
        
    else: 
        print("\nValor inválido!\n")
        
        
def main():
    idade_categoria()
    
if __name__ == '__main__':
    main()