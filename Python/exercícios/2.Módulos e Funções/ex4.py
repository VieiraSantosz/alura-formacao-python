# 4. Solicite ao usuário as coordenadas (x, y) de um ponto qualquer 
# e utilize uma estrutura if elif else para determinar em qual quadrante 
# do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

def coordenadas():

    coord_x = float(input('\nCoordenadas X: '))
    coord_y = float(input('Coordenadas Y: '))

    if (coord_x > 0 and coord_y > 0):
        print('\nPonto localizado no PRIMEIRO QUADRANTE!\n')
        
    elif (coord_x < 0 and coord_y > 0):
        print('\nPonto localizado no SEGUNDO QUADRANTE!\n')
        
    elif (coord_x < 0 and coord_y < 0):
        print('\nPonto localizado no TERCEIRO QUADRANTE!\n')
        
    elif (coord_x > 0 and coord_y < 0):
        print('\nPonto localizado no QUARTO QUADRANTE!\n')
        
    else:
        print('\nPonto localizado no EIXO ou ORGIEM!\n')
        
        
def main():
    coordenadas()
    
if __name__ == '__main__':
    main()