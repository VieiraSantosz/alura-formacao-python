# 9. Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurante:
    nome        = 'Paris'
    categoria   = 'Francesa'
    ativo       = False
    
restaurante_praca = Restaurante()
nome        = restaurante_praca.nome
categoria   = restaurante_praca.categoria


print(f'\nNome do Restaurante.....: {nome}')
print(f'Categoria do Restaurante: {categoria}\n')