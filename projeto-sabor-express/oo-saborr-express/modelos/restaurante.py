from modelos.avaliacao              import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    lista_restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome      = nome.title()
        self._categoria = categoria.upper()
        self._ativo     = False
        self._avaliacao = []
        self._cardapio  = []
        
        Restaurante.lista_restaurantes.append(self)
        
    def __srt__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def exibir_restaurante(cls):
        print(f'\n{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status"}')
        
        for restaurante in cls.lista_restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.estado}\n')
            
    @property
    def estado(self):
        return '☑' if self._ativo else '☒'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if (nota > 5):
            return 0
        
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
     
    @property   
    def media_avaliacao(self):
        if (not self._avaliacao):
            return 'Sem Avaliação'
        
        else:
            soma_notas          = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas    = len(self._avaliacao)
            media_nota          = round(soma_notas / quantidade_notas, 1)    
            return media_nota    
        
    def adicionar_no_cadarpio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do Restaurante {self._nome}\n')
        
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            
