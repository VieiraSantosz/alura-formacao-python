import os

# 1. Crie um dicionário representando informações sobre uma pessoa, 
# como nome, idade e cidade

dicionario_pessoas1 = [
    {'nome': 'Vieira', 'idade': 22, 'cidade': 'São Paulo'},
    {'nome': 'Geovanna', 'idade': 21, 'cidade': 'Rio de Janeiro'}
]


# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

dicionario_pessoas2 = [
    {'nome': 'Vieira', 'idade': '22', 'cidade': 'São Paulo', 'profissao': 'Jogador'},
    {'nome': 'Geovanna', 'idade': '21', 'cidade': 'Rio de Janeiro', 'profissao': 'Modelo'}
]

def listar_opcoes():
    os.system('cls')
    print('\n1. Listar informações das Pessoas.')
    print('2. Alterar idade das Pessoas.')
    print('3. Remover item Pessoas.')
    print('4. Encerrar Programa.')
    
    
def opcao_invalida():
    print('\nOpção Inválida!')
    input('\nDigite qualquer tecla para voltar ao menu. ')
    main()
    
    
def titulo(texto):
    os.system('cls')
    print(texto)
    print()
    

def voltar_menu():
    input('\nDigite qualquer tecla para voltar ao menu. ')
    main()
    
    
def info_pessoas():
    titulo('Listar informações das Pessoas.')
    
    print(f'{"Nome".ljust(10)} | {"Idade".ljust(5)} | {"Cidade".ljust(14)} | {"Profissão"}')
    
    for pessoa in dicionario_pessoas2:
        nome_pessoa         = pessoa['nome']
        idade_pessoa        = pessoa['idade']
        cidade_pessoa       = pessoa['cidade']
        profissao_pessoa    = pessoa['profissao']
        
        print(f'.{nome_pessoa.ljust(9)} | {idade_pessoa.ljust(5)} | {cidade_pessoa.ljust(14)} | {profissao_pessoa}')
    
    voltar_menu()


def alterar_idade():
    titulo('Alterar Idade.')
    
    nome_pessoa = input('Digite o nome da pessoa que deseja alterar a idade: ')
    nome_encontrado = False
    
    for pessoa in dicionario_pessoas2:
        if (nome_pessoa == pessoa['nome']):
            nome_encontrado = True
            
            idade_pessoa    = input(f'Digite a nova idade da(o) {nome_pessoa}: ')
            pessoa['idade'] = idade_pessoa
            
            print('\n[+] Idade alterado com sucesso.')
            
    if (not nome_encontrado):
        print(f'\n[-] O nome {nome_pessoa} não foi encontrado.')
        
    voltar_menu()
    
    
def remover_pessoa():
    titulo('Remover Pessoas.')
    
    nome_remove = input('Digite o nome da pessoa que deseja remover do dicionário: ')
    remove_encontrado = False
    
    for i, pessoa in enumerate(dicionario_pessoas2):
        if(nome_remove == pessoa['nome']):
            remove_encontrado = True
            
            indice_apagar = i
            
            dicionario_pessoas2.pop(indice_apagar)    
            print('\n[+] Pessoa removida com sucesso.')
            
    if (not remove_encontrado):
        print(f'\n[-] O nome {nome_remove} não foi encontrado.')
        
    voltar_menu()
    
    
def encerrar_programa():
    titulo('Programa Encerrado!')


def escolher_opcao():
    try:
        opc = int(input('\nEscolha sua opção: '))
        print(f'Opção Escolhida: {opc}')
    
        match opc:
            case 1:
                info_pessoas()
            case 2:
                alterar_idade()
            case 3:
                remover_pessoa()
            case 4:
                encerrar_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
              

def main():
    listar_opcoes()
    escolher_opcao()
    
    
if __name__ == '__main__':
    main()