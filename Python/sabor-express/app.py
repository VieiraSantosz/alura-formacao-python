import os

lista_restaurantes = ['Pizza', 'Bolo']

def exibir_programa():
    print("""

    ░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
    """)

def exibir_opcoes():  
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def encerrar_app(): 
    exibir_subtitulo('Programa Encerrado!')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def opcao_invalida():
    print('Opção Inválida!')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes.')
    
    nome_restaurante = input('Digite o nome do restaurante para cadastrar: ')
    lista_restaurantes.append(nome_restaurante)
    
    print(f'[+] Restaurante {nome_restaurante} cadastrado com sucesso.')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes.')
    
    for restaurante in lista_restaurantes:
        print(f'.{restaurante}')
    
    voltar_menu_principal()

def escolher_opcoes():
    try:
        opc = int(input('Escolha uma opção: '))
        print(f'\nOpção escolhida {opc}')

        match opc:
            case 1:
                cadastrar_novo_restaurante()
                
            case 2:
                listar_restaurantes()
                
            case 3:
                print('Ativar Restaurante:\n')
                
            case 4:
                encerrar_app()

            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    
    
def main():
    os.system('cls')
    exibir_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
