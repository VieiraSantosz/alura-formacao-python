import os

# 4. Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

dicionario_time = [
    {'nome': 'Real Madrid', 'champions': 14, 'estadio': 'Bernabeu'},
    {'nome': 'Liverpool', 'champions': 6, 'estadio': 'Anfield'},
    {'nome': 'Corinthians', 'champions': 0, 'estadio': 'Neo Quimica Arena'}
]

def time():
    if any('nome' in time for time in dicionario_time):
        print("A chave 'nome' existe em pelo menos um dicionário na lista.")
    else:
        print("A chave 'nome' não existe em nenhum dicionário na lista.")
            
            
def main():
    time()
    
if __name__ == '__main__':
    main()