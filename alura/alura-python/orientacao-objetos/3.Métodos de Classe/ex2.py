# 2. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular    = titular
        self.saldo      = float(saldo)
        self.ativo      = False