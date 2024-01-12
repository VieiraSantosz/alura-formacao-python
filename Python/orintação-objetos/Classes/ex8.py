# 8. Mude o estado da instância restaurante_pizza para ativo.

class Restaurante:
    nome        = ''
    categoria   = ''
    ativo       = True
    
restaurante_pizza = Restaurante()
restaurante_pizza.nome      = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


print(f'\nNome do Restaurante.....: {restaurante_pizza.nome}')
print(f'Categoria do Restaurante: {restaurante_pizza.categoria}')

if (restaurante_pizza.ativo == True):
    print('Estado do Restaurante...: Ativo\n')
    
else:
    print('Estado do Restaurante...: Inativo\n')