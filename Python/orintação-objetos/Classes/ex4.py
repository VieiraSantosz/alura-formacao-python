# 4. Acesse o valor do atributo de classe categoria diretamente da 
# classe Restaurante e armazene em uma variável chamada categoria.

class Restaurante:
    nome        = 'Outback'
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