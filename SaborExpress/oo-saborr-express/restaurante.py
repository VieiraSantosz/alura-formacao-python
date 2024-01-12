class Restaurante:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome      = nome.title()
        self._categoria = categoria.upper()
        self._ativo     = False
        
        Restaurante.lista_restaurantes.append(self)
        
    def __srt__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def exibir_restaurante(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(20)} | {"Status"}')
        
        for restaurante in Restaurante.lista_restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(20)} | {restaurante.estado}')
            
    @property
    def estado(self):
        return '☑' if self._ativo else '☒'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    
restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.alterar_estado()

restaurante_pizza = Restaurante('pizza Express', 'italiana')


Restaurante.exibir_restaurante()