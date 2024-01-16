# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

class Restaurante:
    nome        = ''
    categoria   = ''
    ativo       = False
    
restaurante_pizza = Restaurante()
restaurante_pizza.nome      = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


if (restaurante_pizza.categoria == 'Fast Food'):
    print('\nCategoria é Fast Food\n')
    
else:
    print('\nCategoria não é Fast Food\n')