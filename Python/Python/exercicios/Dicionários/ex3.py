# 3. Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

dicionario_numeros = [
    {'numero': 1, 'quadrado': 1**2},
    {'numero': 2, 'quadrado': 2**2},
    {'numero': 3, 'quadrado': 3**2},
    {'numero': 4, 'quadrado': 4**2},
    {'numero': 5, 'quadrado': 5**2}
]

def quadrado():
    print()
    for numero in dicionario_numeros:
        num = numero['numero']
        qua = numero['quadrado']
        
        print(f'O quadro de {num} = {qua}')
        
    print()
        

def main():
    quadrado()
    
if __name__ == '__main__':
    main()