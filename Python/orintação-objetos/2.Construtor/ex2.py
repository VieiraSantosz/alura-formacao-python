# 2. Implemente uma classe chamada Carro com os atributos básicos, 
# como modelo, cor e ano. Crie uma instância dessa classe e atribua 
# valores aos seus atributos.

class Carro:
    modelo  = ''
    cor     = ''
    ano     = ''
    
mercedes = Carro()
mercedes.modelo = 'A45'
mercedes.cor    = 'Prata'
mercedes.ano    = 2020

bmw = Carro()
bmw.modelo = 'X6'
bmw.cor    = 'Azul'
bmw.ano    = 2022


print(f'\nMercedes - {mercedes.modelo} | {mercedes.cor} | {mercedes.ano}')
print(f'Bmw - {bmw.modelo} | {bmw.cor} | {bmw.ano}\n')