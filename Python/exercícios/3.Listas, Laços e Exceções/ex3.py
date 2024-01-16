# 3. Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def soma_impar():
    soma = 0
    
    for numero in lista_numeros:
        if (numero % 2 == 1):
            soma = soma + numero
            
    print(f"\nSoma dos números ímpares: {soma}\n")
        
        
def main():
    soma_impar()
    
if __name__ == '__main__':
    main()