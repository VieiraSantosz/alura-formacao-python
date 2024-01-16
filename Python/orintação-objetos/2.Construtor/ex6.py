# 6. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe 
# e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.nome       = nome
        self.cpf        = cpf
        self.email      = email
        self.telefone   = int(telefone)
        
    def __str__(self):
        return f'Cliente - {self.nome} | {self.cpf} | {self.email} | {self.telefone}'
    
vieira = Cliente('Wesley Vieira', '123.345.678.90', 'vieira@gmail.com', 11982345678)

print(vieira)