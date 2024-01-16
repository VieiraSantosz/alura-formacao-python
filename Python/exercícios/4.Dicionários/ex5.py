# 5. Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

dicionarios_frase = {'Ignore o orgulho e comece a viver.'}

def frequencia_palavra():
    palavra = 0
    
    for caractere in dicionarios_frase:
        frase = caractere
        
        for i in frase:
            if i.isspace():
                palavra += 1
                
    print(f'\nFrase: {frase}')
    print(f'Quantidade de palavras: {palavra+1}\n')
          
    
def main():
    frequencia_palavra()
    
if __name__ == '__main__':
    main()