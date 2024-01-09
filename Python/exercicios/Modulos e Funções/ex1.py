# 1. Solicite ao usuário que insira um número e, em seguida, 
# use uma estrutura if else para determinar se o número é par ou ímpar.

def par_impar():
    
    numero = int(input('\nDigite un número: '))

    if (numero % 2 == 0):
        print(f'\nO número {numero} é par!\n')

    else:
        print(f'\nO número {numero} é ímpar!\n')
        

def main():
    par_impar()
    
if __name__ == '__main__':
    main()