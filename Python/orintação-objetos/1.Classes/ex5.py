# 5. Altere o valor do atributo nome para 'Bistrô'.

class Restaurante:
    nome        = 'Bistrô'
    categoria   = 'Italiana'
    ativo       = False
    
restaurante_praca = Restaurante()
nome        = restaurante_praca.nome
categoria   = restaurante_praca.categoria


print(f'\nNome do Restaurante.....: {nome}')
print(f'Categoria do Restaurante: {categoria}')

if (restaurante_praca.ativo == True):
    print('Estado do Restaurante...: Ativo\n')
    
else:
    print('Estado do Restaurante...: Inativo\n')