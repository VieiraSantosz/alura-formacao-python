# 1. Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, 
# aproveitando a sintaxe simplificada do Python.

'''
class Musica:
    nome = ''
    artista = ''
    duracao = int
'''

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome       = nome
        self.artista    = artista
        self.duracao    = float(duracao)
        
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
trap = Musica('Novo Balanço', 'Veigh', 2.49)
funk = Musica('Maça Verde', 'Hariel', 3.21)

print(trap)
print(funk)