# 4. Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def numero_descrescente():
    for numero in range(10, 0, -1):
        print(numero)
        

def main():
    numero_descrescente()
    
if __name__ == '__main__':
    main()