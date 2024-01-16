# 3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca 
# e exiba uma mensagem informando se o restaurante está ativo ou inativo.

class Restaurante:
    nome        = 'Outback'
    categoria   = ''
    ativo       = False
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'
nome = restaurante_praca.nome


print(f'\nNome do Restaurante.....: {nome}')
print(f'Categoria do Restaurante: {restaurante_praca.categoria}')

if (restaurante_praca.ativo == True):
    print('Estado do Restaurante...: Ativo\n')
    
else:
    print('Estado do Restaurante...: Inativo\n')