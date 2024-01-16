# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

class Restaurante:
    nome        = 'Outback'
    categoria   = ''
    ativo       = False
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'
nome = restaurante_praca.nome

print(f'\nNome do Restaurante.....: {nome}')
print(f'Categoria do Restaurante: {restaurante_praca.categoria}\n')