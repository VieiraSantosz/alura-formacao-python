# 6. Adicione uma propriedade chamada titular à classe ContaBancaria utilizando a função property. 
# Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular    = titular
        self._saldo      = float(saldo)
        self._ativo      = False
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    @property
    def ativar_conta(self):
        self._ativo = not self._ativo
        

pessoa = ContaBancaria('Vieira', 5000)
print(f'\nNome do Titular - {pessoa.titular}\n')