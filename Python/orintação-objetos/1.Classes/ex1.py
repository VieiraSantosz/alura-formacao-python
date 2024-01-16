# 1. Atribua o valor 'Italiana' ao atributo categoria da instância 
# restaurante_praca da classe Restaurante.

class Restaurante:
    nome        = ''
    categoria   = ''
    ativo       = False
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

print(f'\nCategoria do Restaurante: {restaurante_praca.categoria}\n')