# 5. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.

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