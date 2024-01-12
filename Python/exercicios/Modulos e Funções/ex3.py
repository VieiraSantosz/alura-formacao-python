# 3. Solicite um nome de usuário e uma senha e use uma estrutura if else 
# para verificar se o nome de usuário e a senha fornecidos correspondem 
# aos valores esperados determinados por você.

N1  = 'Vieira'
S1  = 5527

def credencial():
    
    nome    = input('\nDigite un nome de usuário: ')
    senha   = int(input('Digite uma senha: '))

    if (N1 == nome and S1 == senha):
        print('\nNome de usuário e Senhas corretas!\n')
        
    else:
        print('\nTente novamente! Nome ou Senha estão incorretas.\n')
        

def main():
    credencial()
    
if __name__ == '__main__':
    main()