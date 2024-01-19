# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza 
# com o nome 'Pizza Place' e categoria 'Fast Food'.

class Restaurante:
    nome        = ''
    categoria   = ''
    ativo       = False
    
restaurante_pizza = Restaurante()
restaurante_pizza.nome      = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


print(f'\nNome do Restaurante.....: {restaurante_pizza.nome}')
print(f'Categoria do Restaurante: {restaurante_pizza.categoria}')

if (restaurante_pizza.ativo == True):
    print('Estado do Restaurante...: Ativo\n')
    
else:
    print('Estado do Restaurante...: Inativo\n')