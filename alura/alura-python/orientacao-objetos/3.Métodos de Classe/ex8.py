# 8. Crie um método de classe para a conta ClienteBanco.

class ClienteBanco:
    lista_clientes = []
    
    def __init__(self, nome, data_nascimento, cpf, banco, saldo):
        self._nome               = nome
        self._data_nascimento    = data_nascimento
        self._cpf                = cpf
        self._banco              = banco
        self._saldo              = float(saldo)
        
        ClienteBanco.lista_clientes.append(self)
        
    def __str__(self):
        return f'Nome: {self._nome}, Data: {self._data_nascimento}, Cpf: {self._cpf}, Banco: {self._banco}, Saldo: {self._saldo}'
    
    @classmethod
    def exibir_clientes(cls):
        print('\nInformações dos Clientes:')
        
        for cliente in cls.lista_clientes:
            print(f'Titular: {cliente._nome.ljust(10)} | Cpf: {cliente._cpf.ljust(10)} | Data: {cliente._data_nascimento}')
            
    

clinte1 = ClienteBanco('Vieira', '02/05/2002', '567.435.678-90', 'Itau', 3500)
clinte2 = ClienteBanco('Veigh', '15/07/2000', '456.234.876-83', 'Bradesco', 5700)
clinte3 = ClienteBanco('Vini', '22/02/2004', '356.167.478-12', 'Nubank', 12500)

ClienteBanco.exibir_clientes()