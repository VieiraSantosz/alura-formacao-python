# 3. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e 
# crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    nome            = ''
    categoria       = ''
    ativo           = ''
    endereco        = ''
    classificacao   = ''
    
outbakc = Restaurante()
outbakc.nome            = 'Outback Tatuapé'
outbakc.categoria       = 'Steakhouse'
outbakc.ativo           = 'Ativado'
outbakc.endereco        = 'R. Gonçalves Crespo, 78'
outbakc.classificacao   = 4.5

print(vars(outbakc))