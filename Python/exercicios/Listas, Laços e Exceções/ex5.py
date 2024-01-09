# 5. Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir 
# a tabuada desse número, indo de 1 a 10.

numero = int(input('\nDigite um número: '))

for i in range(1, 11, 1):
    soma = i * numero
    print(f'{i} * {numero} = {soma}')
    