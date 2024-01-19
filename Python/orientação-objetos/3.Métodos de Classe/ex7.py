# 7. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    
    def __init__(self, nome, data_nascimento, cpf, banco, saldo):
        self._nome               = nome
        self._data_nascimento    = data_nascimento
        self._cpf                = cpf
        self._banco              = banco
        self._saldo              = float(saldo)
        
    def __str__(self):
        return f'Nome: {self._nome}, Data: {self._data_nascimento}, Cpf: {self._cpf}, Banco: {self._banco}, Saldo: {self._saldo}'    
    

cliente1 = ClienteBanco('Vieira', '02/05/2002', '567.435.678-90', 'Itau', 3500)
cliente2 = ClienteBanco('Veigh', '15/07/2000', '456.234.876-83', 'Bradesco', 5700)
cliente3 = ClienteBanco('Vini', '22/02/2004', '356.167.478-12', 'Nubank', 12500)

print('\nInformações dos Clientes:')
print(cliente1)
print(cliente2)
print(cliente3)
print()