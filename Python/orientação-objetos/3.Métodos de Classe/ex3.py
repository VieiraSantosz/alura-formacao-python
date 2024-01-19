# 3. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada 
# com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular    = titular
        self.saldo      = float(saldo)
        self.ativo      = False
        
    def __str__(self):
        return f'Conta Bancária: {self.titular} | {self.saldo} | {self.ativo}'
    
    
pessoa1 = ContaBancaria('Vieira', 3450)
pessoa2 = ContaBancaria('Veigh', 10780.60)
print()
print(pessoa1)
print(pessoa2)
print()