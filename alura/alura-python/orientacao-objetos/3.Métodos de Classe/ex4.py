# 4. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que 
# define o atributo ativo como True. Crie uma instância da classe, chame o método de classe 
# e imprima o valor de ativo.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular    = titular
        self.saldo      = float(saldo)
        self.ativo     = False
        
    def __str__(self):
        return f'Conta Bancária: {self.titular} | {self.saldo} | {self.ativo}'
    
    @classmethod
    def ativar_conta(self, conta):
        conta.ativo = not conta.ativo
    
    
pessoa1 = ContaBancaria('Vieira', 3450)
pessoa1.ativar_conta(pessoa1)
pessoa2 = ContaBancaria('Veigh', 10780.60)
print()
print(pessoa1)
print(pessoa2)
print()