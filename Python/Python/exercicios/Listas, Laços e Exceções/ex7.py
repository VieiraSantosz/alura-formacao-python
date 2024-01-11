# 7. Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.

lista_numero = [5, 10, 15, 20, 25]

def media_numero():
    soma    = 0
    cont    = 0
    
    try:
        for numero in lista_numero:
            soma = soma + numero
            cont += 1
            
        media = soma / cont
        print(f'\nMédia da Soma: {media}\n')
        
    except ZeroDivisionError:
        print('\nLista está vazia!\n')
        
    except Exception as erro:
        print(f'\nErro de Cálculo: {erro}\n')
    
    
def main():
    media_numero()
    
if __name__ == '__main__':
    main()