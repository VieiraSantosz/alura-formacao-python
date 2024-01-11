# 6. Crie uma lista de números e utilize um loop for para calcular a soma de todos 
# os elementos.Utilize um bloco try-except para lidar com possíveis exceções.

lista_numero = [2, 4, 8, 16, 32, 64]

def soma_numero():
    soma = 0
    
    try:
        for numero in lista_numero:
            soma = soma + numero
            
        print(f'\nSoma Total: {soma}\n')
            
    except Exception as erro:
        print(f'\nErro de Cálculo: {erro}\n')
        
        
def main():
    soma_numero()
    
if __name__ == '__main__':
    main()