import os

lista_restaurantes = ['Pizza', 'Bolo']

dicionario_restaurantes = [
                {'nome': 'Praça', 'categoria': 'Japones', 'ativo': False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Brasileiro', 'ativo': False}
            ]

def exibir_programa():
    print("""

    ░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
    """)


def exibir_opcoes():  
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurante')
    print('3. Alterar estado Restaurante')
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
    linha = '*' * (len(texto) + 4)
    print(f'{linha}\n')
    print(texto)
    print(f'\n{linha}')
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes.')
    
    nome        = input('Digite o nome do restaurante para cadastrar: ')
    categoria   = input(f'Digite a categoria do restaurante {nome} para cadastrar: ')
    
    dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    dicionario_restaurantes.append(dados_restaurante)
    
    print(f'\n[+] Restaurante {nome} cadastrado com sucesso.')
    voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes.')
    
    print(f'{"Nome do restaurante".ljust(21)} | {"Categoria".ljust(20)} | Status\n')
    
    for restaurante in dicionario_restaurantes:
        nome_restaurante        = restaurante['nome']
        categoria_restaurante   = restaurante['categoria']
        ativo_restaurante       = 'Ativado' if restaurante['ativo'] else 'Desativado'
        
        print(f'.{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    
    voltar_menu_principal()


def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante.')
    
    nome_restaurante = input('Digite o nome do restaunte que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in dicionario_restaurantes:
        if (nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            
            restaurante['ativo'] = not restaurante['ativo']
            
            if (restaurante['ativo']):
                mensagem = f'\n [+] O restaurente {nome_restaurante} foi ATIVADO com sucesso.'
            else:
                mensagem = f'\n[+] O restaurante {nome_restaurante} foi DESATIVADO com sucesso.'
                
            print(mensagem)
            
    if (not restaurante_encontrado):
        print(f'\n[-] O restaurante {nome_restaurante} não foi encontrado.')
            
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
                alterar_estado_restaurante()
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
